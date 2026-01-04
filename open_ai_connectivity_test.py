import asyncio
from fastmcp import Client
import json

client = Client("http://localhost:8000/mcp")

async def test_ai_analysis_tool():
    """
    Specific test to verify if the analyze_with_ai tool works correctly
    independent of Dify Cloud.
    """
    async with client:
        print("\n4. Testing analyze_with_ai (Direct Call)...")
        print("-" * 60)
        
        # We first need to get some data context, usually Dify does this via SQL
        # checking logic, but for the test we will simulate a simple question.
        
        user_question = "What is the best selling product category?"
        
        # In a real flow, 'data_context' comes from a previous SQL query.
        # We will pass a raw string to simulate what the tool expects.
        dummy_data_context = """
        Product Category, Total Revenue
        Electronics, 50000
        Clothing, 20000
        Books, 5000
        """

        try:
            # Call the tool with the arguments defined in my_server.py
            result = await client.call_tool("analyze_with_ai", {
                "user_question": user_question,
                "data_context": dummy_data_context
            })
            
            analysis = result.content[0].text
            print("Received Analysis from Server:")
            print(analysis)
            
            if "summary" in analysis.lower():
                print("\n[PASS] Structure looks correct (contains headers).")
            else:
                print("\n[WARNING] Response format might be incorrect.")
                
        except Exception as e:
            print(f"Error calling analyze_with_ai: {e}")

# Don't forget to add this to your main execution block
# asyncio.run(test_ai_analysis_tool())

if __name__ == "__main__":
    asyncio.run(test_ai_analysis_tool())
