from pydantic import BaseModel
from enum import Enum

class Category(str, Enum):
    politics = "Politics"
    business = "Business"
    technology = "Technology"
    health = "Health"
    sports = "Sports"
    entertainment = "Entertainment"
    science = "Science"
    other = "Other"

class Sentiment(str, Enum):
    positive = "Positive"
    negative = "Negative"
    neutral = "Neutral"

class NewsArticle(BaseModel):
    title: str
    url: str
    source: str
    summary: str
    full_content: str
    category: Category
    sentiment: Sentiment
    published_at: str

class NewsFeed(BaseModel):
    title: str
    url: str
    source: str
    description: str
    category: Category
    sentiment: Sentiment
    published_at: str
