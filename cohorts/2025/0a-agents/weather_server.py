import asyncio
from fastmcp import FastMCP, Client
import random


known_weather_data = {"berlin": 20.0}
mcp = FastMCP("Demo 🚀")


@mcp.tool
def get_weather(city: str) -> float:
    """
    Retrieves the temperature for a specified city.

    Parameters:
        city (str): The name of the city for which to retrieve weather data.

    Returns:
        float: The temperature associated with the city.
    """
    print("asd")
    city = city.strip().lower()

    if city in known_weather_data:
        return known_weather_data[city]
    return round(random.uniform(-5, 35), 1)


@mcp.tool
def set_weather(city: str, temp: float) -> None:
    """
    Sets the temperature for a specified city.

    Parameters:
        city (str): The name of the city for which to set the weather data.
        temp (float): The temperature to associate with the city.

    Returns:
        str: A confirmation string 'OK' indicating successful update.
    """
    city = city.strip().lower()
    known_weather_data[city] = temp
    return "OK"


async def main():
    async with Client(mcp) as mcp_client:
        tools = await mcp_client.list_tools()
        print(f"{tools = }")
        mcp_tools = await mcp_client.list_tools_mcp()
        print(f"{mcp_tools = }")


if __name__ == "__main__":
    test = asyncio.run(main())
