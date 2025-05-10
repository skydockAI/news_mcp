import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or "Enter your OpenAI API key here"
    OPENAI_MODEL = os.getenv("OPENAI_MODEL") or "gpt-4o"
    OPENAI_MINI_MODEL = os.getenv("OPENAI_MINI_MODEL") or "gpt-4o-mini"
    USER_AGENT_STRING = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    RSS_FEEDS = [
        {
            "name": "CBC",
            "url": "https://www.cbc.ca/webfeed/rss/rss-topstories"
        },
        {
            "name": "BBC",
            "url": "https://feeds.bbci.co.uk/news/rss.xml"
        },
        {
            "name": "TechCrunch",
            "url": "https://techcrunch.com/feed/"
        }
    ]


