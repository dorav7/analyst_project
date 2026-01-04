import asyncio
from fastmcp import Client
import json

client = Client("http://localhost:8000/mcp")

async def test_data_analyst_tools():
    async with client:
        print("=" * 60)
        print("Testing Data Analyst MCP Server")
        print("=" * 60)
        
        print("\n1. Testing get_data_schema()...")
        print("-" * 60)
        try:
            result = await client.call_tool("get_data_schema", {})
            schema = result.content[0].text
            print(json.dumps(json.loads(schema), indent=2))
        except Exception as e:
            print(f"Error: {e}")
        
        print("\n2. Testing perform_aggregation()...")
        print("-" * 60)
        try:
            result = await client.call_tool("perform_aggregation", {
                "group_by": "Product Category",
                "target_column": "Total Revenue",
                "operation": "sum"
            })
            aggregation = result.content[0].text
            print(json.dumps(json.loads(aggregation), indent=2))
        except Exception as e:
            print(f"Error: {e}")
        
        print("\n3. Testing generate_chart_config()...")
        print("-" * 60)
        try:
            result = await client.call_tool("generate_chart_config", {
                "chart_type": "bar",
                "x_axis": "Product Category",
                "y_axis": "Total Revenue",
                "title": "Sales by Product Category"
            })
            chart_config = result.content[0].text
            print(json.dumps(json.loads(chart_config), indent=2))
        except Exception as e:
            print(f"Error: {e}")
        
        print("\n" + "=" * 60)
        print("Testing Complete")
        print("=" * 60)

if __name__ == "__main__":
    asyncio.run(test_data_analyst_tools())
