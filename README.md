# News MCP
**News MCP** is an open-source Model Context Protocol (MCP) server that retrieves and extracts structured information from RSS news feeds and full-length articles. Designed to serve as a tool provider for AI agents, News MCP can summarize and analyze news content using OpenAI models.

## ✨ Features
- Retrieve curated RSS news feeds (CBC, BBC, TechCrunch, etc.)
- Extract and structure full article content from news URLs
- Use OpenAI models to summarize, categorize, and analyze sentiment
- Built-in tools compatible with any MCP-compatible agent or client
- Example included to interact via SSE using `MCPServerSse`

## 🧰 Available Tools
**get_news_rss_list()-> list** : Returns the list of configured RSS feed sources.

**get_news_feeds(rss_url: str) -> list[]**: Fetches and parses RSS feed items using OpenAI to extract structured content.

**get_news_article(article_url: str) -> NewsArticle**: Fetches a full article from a URL and uses OpenAI to extract a structured article object, including:
- Title
- URL and Source
- Summary and Full Content
- Category
- Sentiment
- Publish Date

## 🚀 Getting Started
Clone the repository:
```bash
git clone https://github.com/skydockAI/news_mcp.git
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Set your OpenAI API key or edit [config.py](config.py):
```bash
export OPENAI_API_KEY="your-api-key-here"
```

(Optional) Set OpenAI models that you want to use:
```bash
export OPENAI_MODEL="gpt-4o"
export OPENAI_MINI_MODEL="gpt-4o-mini"
```

(Optional) Add more RSS news feeds that you want to use in [config.py](config.py)

## 🏃 Running the MCP Server
```bash
python news_mcp_server.py
```

The server will run on http://localhost:8000/sse using Server-Sent Events (SSE) transport.

## 🧪 Example Usage
You can run the [examples.py](examples.py) script to test the server:

```bash
python examples.py
```

Example instruction:
```
Create a one paragraph summary of the latest news about AI from TechCrunch and list out all the sources at the end
```

Result:
```
OpenAI's presence in the enterprise AI market is significantly growing, with over 32% of U.S. businesses now subscribing to its products, as reported by Ramp's AI Index. The rapid adoption is seen with a leap from 18.9% in January to 32.4% in April 2025, while competitors like Anthropic and Google AI have struggled to maintain similar traction. OpenAI expects its enterprise revenue, projected at $12.7 billion for the year, to contribute to long-term growth despite not anticipating profitability until 2029. In other news, the U.S. Treasury Department is reviewing Benchmark's $75 million investment in Chinese AI startup Manus amid concerns about compliance with newer restrictions on Chinese investments. Manus claims compliance by structuring operations in the Cayman Islands and focusing on a "wrapper" around existing AI models rather than developing its own.

Sources:
- [OpenAI's enterprise adoption appears to be accelerating, at the expense of rivals](https://techcrunch.com/2025/05/10/openai-enterprise-adoption-accelerating/)
- [The US is reviewing Benchmark’s investment into Chinese AI startup Manus](https://techcrunch.com/2025/05/09/us-review-benchmark-investment-manus-ai/)
```

## ⚠️ Disclaimer
The **get_news_article** function in this project is intended solely for educational and research purposes. It retrieves publicly available article content from third-party news websites. Users are solely responsible for ensuring that their use of this tool complies with the terms of service of any website it accesses.

The maintainer of this project does not assume any liability for misuse or legal consequences resulting from third-party use.

## 🔓 License
This project is released under the [MIT License](LICENSE). You are free to use, modify, and distribute this software.

