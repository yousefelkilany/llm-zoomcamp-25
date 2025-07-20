import asyncio
from fastmcp import Client
from weather_server import mcp


async def main():
    async with Client(mcp) as mcp_client:
        tools = await mcp_client.list_tools()
        print(f"{tools = }")
        mcp_tools = await mcp_client.list_tools_mcp()
        print(f"{mcp_tools = }")


if __name__ == "__main__":
    test = asyncio.run(main())
