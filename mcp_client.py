import os 
import asyncio

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

client = MultiServerMCPClient(
    {
        "tavily": {
            "transport": "streamable_http",
            "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={TAVILY_API_KEY}"
        } 





    }
)


# async def main():
#     tools = await client.get_tools()
#     print("\nAvailable MCP Tools:\n")
#     for tool in tools:
#         print(tool.name)


async def main():
    tools = await client.get_tools()
    print("\nAvailable MCP Tools:\n")
    search_tool = next(
        tool
        for tool in tools
        if tool.name == "tavily_search"
    )
    result = await search_tool.ainvoke(
        {
            "query": "Best hotels in Delhi"
        }
    )
    print(result)

asyncio.run(main())

if __name__ == "__main__":
    asyncio.run(main())