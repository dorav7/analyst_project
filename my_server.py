import pandas as pd
import duckdb
from fastmcp import FastMCP
import os
from dotenv import load_dotenv 
load_dotenv()


TABLE_NAME = 'data'

mcp = FastMCP("My MCP Server")

CSV_FILE_PATH = "Online Sales Data.csv"

@mcp.tool
def get_data_schema() -> dict:
    """
    Scans the CSV file and returns comprehensive metadata about the dataset.
    ALWAYS run this tool first to understand the column names.
    """
    try:
        if not os.path.exists(CSV_FILE_PATH):
             return {"error": f"CSV file not found: {CSV_FILE_PATH}"}

        df = pd.read_csv(CSV_FILE_PATH)
        
        if df.empty:
            return {"error": "CSV file is empty"}
        
        schema = {
            "table_name": TABLE_NAME,
            "columns": list(df.columns),
            "row_count": len(df),
            "column_details": {}
        }
        
        for col in df.columns:
            col_info = {"data_type": str(df[col].dtype)}
            
            if pd.api.types.is_numeric_dtype(df[col]):
                col_info["min"] = float(df[col].min())
                col_info["max"] = float(df[col].max())
                col_info["sample_values"] = df[col].dropna().head(3).tolist()
            else:
                unique_vals = df[col].dropna().unique()
                col_info["unique_count"] = len(unique_vals)
                col_info["sample_values"] = unique_vals[:5].tolist()
            
            schema["column_details"][col] = col_info
        
        return schema
    
    except Exception as e:
        return {"error": f"Error reading CSV: {str(e)}"}

@mcp.tool
def run_sql_query(query: str) -> str:
    """
    Executes a SQL query on the CSV data and returns text results.
    """
    try:
        con = duckdb.connect(database=':memory:')
        con.execute(f"CREATE TABLE {TABLE_NAME} AS SELECT * FROM read_csv_auto('{CSV_FILE_PATH}')")
        result_df = con.execute(query).df()
        
        if result_df.empty:
            return "Query executed successfully but returned no results."
            
        return result_df.to_markdown(index=False)
        
    except Exception as e:
        return f"SQL Error: {str(e)}"


@mcp.tool
def analyze_with_ai(data_context: str, user_question: str = "") -> str:
    """
    Sends data to OpenAI with strict safety limits and debug prints.
    """
    from openai import OpenAI
    import os

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "Error: OPENAI_API_KEY not set."

    print(f"DEBUG: Starting AI Analysis...")
    print(f"DEBUG: Original data length: {len(data_context)} characters")

    
    if len(data_context) > 4000:
        data_context = data_context[:4000] + "\n... [Data Truncated due to Rate Limits] ..."
        print("DEBUG: Data was truncated to 4000 chars.")

    try:
        client = OpenAI()
        
        response = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[
                {"role": "system", "content": """You are a helpful data analyst. Always format your response with these exact subtitles:
- summary
- insights  
- recommendations

Under each subtitle, provide relevant content. Be concise and specific."""},
                {"role": "user", "content": f"Question: {user_question}\nData:\n{data_context}"}
            ],
            temperature=0.3,
            max_tokens=1000 
        )

        print("DEBUG: Success! Got response from OpenAI.")
        return response.choices[0].message.content

    except Exception as e:
        error_msg = str(e)
        print(f"DEBUG ERROR: {error_msg}")
        
        if "rate_limit" in error_msg.lower():
            return "⚠️ OpenAI Rate Limit Reached. Wait a moment or reduce data size."
        if "insufficient_quota" in error_msg.lower():
            return "⚠️ OpenAI Error: You ran out of credits (Check Billing)."
            
        return f"Error calling OpenAI: {error_msg}"

    except Exception as e:
        if "rate_limit" in str(e).lower():
            return "⚠️ System is busy (Rate Limit). Please try asking for a smaller dataset or wait a few seconds."
        return f"Error calling OpenAI: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
