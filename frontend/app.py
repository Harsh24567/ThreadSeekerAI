import streamlit as st
from components.search import search_section
from components.results import display_results
from components.theme import setup_page
from utils.api import search_threads, live_search
import json

def main():
    # Setup page theme and configuration
    setup_page()
    
    # App title and description
    st.markdown(
        """
        <div class="header-container">
            <h1 class="main-title">ThreadSeekerAI</h1>
            <p class="subtitle">Discover intelligent threads on any topic using AI</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Initialize session state for storing results
    if 'search_results' not in st.session_state:
        st.session_state.search_results = []
    
    if 'is_searching' not in st.session_state:
        st.session_state.is_searching = False
    
    # Search interface
    query, search_mode = search_section()
    
    # Perform search when form is submitted
    if query:
        with st.spinner("Searching for threads..."):
            st.session_state.is_searching = True
            
            if search_mode == "Semantic Search":
                results = search_threads(query)
            else:  # Live Search
                results = live_search(query)
            
            st.session_state.search_results = results
            st.session_state.is_searching = False
    
    # Display results
    if st.session_state.search_results:
        display_results(st.session_state.search_results)

if __name__ == "__main__":
    main()