import requests # type: ignore
import json
from typing import Dict, List, Any, Optional
import random

SEARCH_ENDPOINT = "/search"
LIVE_ENDPOINT = "/live"

BASE_URL = "http://localhost:5000"  

def search_threads(query: str) -> List[Dict[str, Any]]:
    try:
        response = requests.post(
            f"{BASE_URL}{SEARCH_ENDPOINT}",
            json={"query": query},
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.exceptions.RequestException as e:
        print(f"[Fallback] Using mock results for '{query}' in semantic mode due to error: {e}")
        return generate_mock_results(query, "semantic")

def live_search(query: str) -> List[Dict[str, Any]]:
    try:
        response = requests.post(
            f"{BASE_URL}{LIVE_ENDPOINT}",
            json={"query": query},
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.exceptions.RequestException as e:
        print(f"[Fallback] Using mock results for '{query}' in live mode due to error: {e}")
        return generate_mock_results(query, "live")


def generate_mock_results(query: str, mode: str) -> List[Dict[str, Any]]:
    """
    Generate mock results for demonstration purposes
    
    Args:
        query: The search query
        mode: The search mode ("semantic" or "live")
        
    Returns:
        A list of mock thread results
    """
    topics = {
        "machine learning": ["AI", "Data Science", "Neural Networks", "Deep Learning"],
        "climate change": ["Environment", "Global Warming", "Sustainability", "Science"],
        "cryptocurrency": ["Bitcoin", "Blockchain", "Finance", "Technology"],
        "health": ["Wellness", "Medicine", "Fitness", "Nutrition"],
        "politics": ["Government", "Democracy", "Policy", "Election"],
        "gaming": ["Video Games", "Esports", "Entertainment", "Technology"],
    }
    
    default_tags = ["Technology", "Discussion", "Trending"]
    
    relevant_topic = None
    for topic in topics:
        if topic.lower() in query.lower():
            relevant_topic = topic
            break
    
    tags = topics.get(relevant_topic, default_tags)
    
    source = "Reddit" if mode == "semantic" else "News"
    recency = "2 days ago" if mode == "semantic" else "2 hours ago"
    
    results = []
    for i in range(10):
        result_tags = random.sample(tags, min(3, len(tags)))
        
        general_tags = ["Trending", "Popular", "Discussion", "Analysis", "Question"]
        result_tags.append(random.choice(general_tags))
        
        results.append({
            "title": f"{'Latest ' if mode == 'live' else ''}{query.title()} {random.choice(['Discussion', 'Analysis', 'Overview', 'Guide', 'Question'])} {i+1}",
            "content": f"This is a {'real-time' if mode == 'live' else 'highly relevant'} thread about {query}. It contains valuable insights and information that matches your search criteria. The community has been actively discussing this topic with various perspectives and expertise.",
            "tags": result_tags,
            "source": source,
            "timestamp": recency,
            "relevance_score": round(random.uniform(0.7, 0.99), 2)
        })
    
    return results