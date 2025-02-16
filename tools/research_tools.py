from datetime import datetime
import requests
from langchain_core.tools import tool
from config import PERPLEXITY_API_KEY

@tool
def get_current_date(query: str) -> str:
    """Retrieves current date in YYYY-MM-DD format"""
    return datetime.now().strftime("%Y-%m-%d")

@tool
def perplexity_research(query: str) -> str:
    """Performs industry research using Perplexity API"""
    url = "https://api.perplexity.ai/chat/completions"
    
    messages = [
        {
            "role": "system",
            "content": """Analyst Assistant. Provide structured analysis of:
- Recent sector trends
- Company-specific developments
- Upcoming events
- Market sentiment"""
        },
        {
            "role": "user",
            "content": f"{query} - Current date: {datetime.now().strftime('%Y-%m-%d')}"
        }
    ]
    
    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-sonar-small-128k-online",
            "messages": messages
        }
    )
    return response.json()['choices'][0]['message']['content']