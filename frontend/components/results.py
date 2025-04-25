import streamlit as st
import random

def get_tag_color(tag):
    """Generate consistent color for tags"""
    tag_colors = {
        "technology": "#3b82f6",  # blue
        "science": "#8b5cf6",     # purple
        "politics": "#ef4444",    # red
        "business": "#f97316",    # orange
        "health": "#10b981",      # green
        "entertainment": "#ec4899",  # pink
        "sports": "#84cc16",      # lime
        "education": "#06b6d4",   # cyan
    }
    
    for key in tag_colors:
        if key in tag.lower():
            return tag_colors[key]
    
    hash_value = sum(ord(c) for c in tag.lower())
    hue = hash_value % 360
    return f"hsl({hue}, 70%, 60%)"

def display_results(results):
    """Display search results as cards"""
    
    st.markdown("## Search Results")
    
    if not results:
        st.info("No results found. Try a different search query.")
        return
    
    st.markdown("""
    <style>
    .result-card {
        background: white;
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .result-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.1);
    }
    
    .card-title {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #1f2937;
    }
    
    .card-content {
        font-size: 0.95rem;
        color: #4b5563;
        margin-bottom: 0.8rem;
        line-height: 1.5;
    }
    
    .tag-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 0.8rem;
    }
    
    .tag {
        border-radius: 20px;
        padding: 0.25rem 0.75rem;
        font-size: 0.75rem;
        font-weight: 500;
        color: white;
        display: inline-flex;
        align-items: center;
    }
    
    .result-source {
        font-size: 0.8rem;
        color: #6b7280;
        margin-top: 0.5rem;
        display: flex;
        align-items: center;
    }
    
    .result-source svg {
        margin-right: 0.3rem;
    }
    
    .result-meta {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 0.5rem;
        font-size: 0.8rem;
        color: #6b7280;
    }
    </style>
    """, unsafe_allow_html=True)
    
    for result in results:
        title = result.get("title", "Untitled Thread")
        content = result.get("content", "No content available")
        tags = result.get("tags", [])
        
        if len(content) > 180:
            content = content[:180] + "..."
        
        source = result.get("source", "Reddit" if random.random() > 0.5 else "News")
        timestamp = result.get("timestamp", "2h ago")
        
        card_html = f"""
        <div class="result-card">
            <div class="card-title">{title}</div>
            <div class="card-content">{content}</div>
            <div class="tag-container">
        """
        
        for tag in tags:
            tag_color = get_tag_color(tag)
            card_html += f'<span class="tag" style="background-color: {tag_color}">{tag}</span>'
        
        source_icon = "📱" if source == "Reddit" else "📰"
        card_html += f"""
            </div>
            <div class="result-meta">
                <div class="result-source">{source_icon} {source}</div>
                <div>{timestamp}</div>
            </div>
        </div>
        """
        
        st.markdown(card_html, unsafe_allow_html=True)