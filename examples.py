from agents import Agent, Runner, set_default_openai_key
from config import Config
import asyncio
from agents.mcp import MCPServerSse
from agents.model_settings import ModelSettings

async def test_mcp_server(instructions: str):
    set_default_openai_key(Config.OPENAI_API_KEY)
    mcp_server = MCPServerSse(
        name="News MCP Server",
        params={
            "url": "http://localhost:8000/sse"
        },
        client_session_timeout_seconds=300, # 5 minutes timeout
    )
    await mcp_server.connect()
    print("Connected to MCP server")

    try:
        agent = Agent(
            name="Test Agent",
            instructions="You are a helpful assistant.",
            model=Config.OPENAI_MODEL,
            mcp_servers=[mcp_server],
            model_settings=ModelSettings(tool_choice="required"),
        )
        result = await Runner.run(agent, instructions)
        print(result.final_output)
    finally:
        await mcp_server.cleanup()

if __name__ == "__main__":
    # asyncio.run(test_mcp_server(f'Create a one paragraph summary of CBC news feeds'))
    asyncio.run(test_mcp_server(f'Create a one paragraph summary of the latest news about AI from TechCrunch and list out all the sources at the end'))
