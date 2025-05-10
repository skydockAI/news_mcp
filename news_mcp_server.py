from mcp.server.fastmcp import FastMCP
from agents import Agent, Runner, set_default_openai_key
from bs4 import BeautifulSoup
import requests
from config import Config
from models import NewsArticle, NewsFeed

mcp = FastMCP("News Retriever Server")
set_default_openai_key(Config.OPENAI_API_KEY)

@mcp.tool()
async def get_news_rss_list() -> list[object]:
    """
    Get the list of news RSS URLs.
    """
    return Config.RSS_FEEDS

@mcp.tool()
async def get_news_feeds(rss_url: str) -> list[NewsFeed]:
    """
    Get news feeds from the RSS URL.
    Args:
        rss_url: The RSS URL to get the news feeds from.
    Returns:
        A list of NewsFeed objects.
    """
    headers = {
        "User-Agent": Config.USER_AGENT_STRING
    }
    response = requests.get(rss_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to get the news feeds from the URL: {rss_url}")
        return []
    agent = Agent(
        name="News Feed Retriever",
        instructions="You are a news feed retriever.",
        model=Config.OPENAI_MINI_MODEL,
        output_type=list[NewsFeed]
    )
    result = await Runner.run(agent, f'Extract the news feeds from raw data and return them in a structured format:\n {response.content}')
    return result.final_output

@mcp.tool()
async def get_news_article(article_url: str) -> NewsArticle:
    """
    Get the news article from the URL.
    Args:
        article_url: The URL of the news article to get.
    Returns:
        A NewsArticle object.
    """
    raw_text = extract_raw_text(article_url)
    agent = Agent(
        name="News Article Retriever",
        instructions="You are a news article retriever.",
        model=Config.OPENAI_MINI_MODEL,
        output_type=NewsArticle
    )
    result = await Runner.run(agent, f'Here is the raw text retrieved from an online news article. Please extract the news article context and return it in a structured format:\n {raw_text}')
    return result.final_output


def extract_raw_text(url: str) -> str:
    headers = {
        "User-Agent": Config.USER_AGENT_STRING
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to get the news article from the URL: {url}")
        return ""
    soup = BeautifulSoup(response.content, 'html.parser')
    # Remove script and style elements
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    # Extract text from the entire HTML content
    text = soup.get_text(separator="\n", strip=True)
    return text

if __name__ == "__main__":
    mcp.run(transport="sse")

