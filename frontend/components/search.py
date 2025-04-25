import streamlit as st
from streamlit_lottie import st_lottie
import json
import os

def load_lottie(filepath):
    """Load a Lottie animation file"""
    with open(filepath, "r") as f:
        return json.load(f)

def search_section():
    """Render the search interface"""
    
    os.makedirs("assets", exist_ok=True)
    
    search_animation = {
        "v": "5.7.8",
        "fr": 30,
        "ip": 0,
        "op": 120,
        "w": 200,
        "h": 200,
        "nm": "Search",
        "ddd": 0,
        "assets": [],
        "layers": [
            {
                "ddd": 0,
                "ind": 1,
                "ty": 4,
                "nm": "Search",
                "sr": 1,
                "ks": {
                    "o": {"a": 0, "k": 100},
                    "r": {
                        "a": 1,
                        "k": [
                            {"t": 0, "s": [0], "e": [360]},
                            {"t": 120, "s": [360]}
                        ]
                    },
                    "p": {"a": 0, "k": [100, 100]},
                    "a": {"a": 0, "k": [0, 0]},
                    "s": {"a": 0, "k": [100, 100, 100]}
                },
                "shapes": [
                    {
                        "ty": "gr",
                        "it": [
                            {
                                "d": 1,
                                "ty": "el",
                                "s": {"a": 0, "k": [80, 80]},
                                "p": {"a": 0, "k": [0, 0]},
                                "nm": "Circle"
                            },
                            {
                                "ty": "st",
                                "c": {"a": 0, "k": [0.4, 0.2, 0.8, 1]},
                                "o": {"a": 0, "k": 100},
                                "w": {"a": 0, "k": 8},
                                "lc": 2,
                                "lj": 1,
                                "ml": 4,
                                "nm": "Stroke"
                            },
                            {
                                "ty": "tr",
                                "p": {"a": 0, "k": [0, 0]},
                                "a": {"a": 0, "k": [0, 0]},
                                "s": {"a": 0, "k": [100, 100]},
                                "r": {"a": 0, "k": 0},
                                "o": {"a": 0, "k": 100}
                            }
                        ],
                        "nm": "Circle"
                    }
                ],
                "op": 120
            }
        ]
    }
    
    with open("assets/search_animation.json", "w") as f:
        json.dump(search_animation, f)
    
    with st.container():
        col1, col2 = st.columns([7, 3])
        
        with col1:
            with st.form(key="search_form"):
                query = st.text_input(
                    "What do you want to explore?",
                    placeholder="Enter your search query...",
                    key="search_query",
                    help="Try topics like 'machine learning', 'climate change', or 'productivity tips'"
                )
                
                col_mode, col_submit = st.columns([3, 1])
                
                with col_mode:
                    search_mode = st.radio(
                        "Search Mode",
                        ["Semantic Search", "Live Search"],
                        horizontal=True,
                        help="Semantic Search uses offline data. Live Search fetches real-time data."
                    )
                
                with col_submit:
                    search_button = st.form_submit_button(
                        label="Search",
                        use_container_width=True,
                        type="primary"
                    )
        
        with col2:
            try:
                lottie_search = load_lottie("assets/search_animation.json")
                st_lottie(
                    lottie_search,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="high",
                    height=150,
                    key="search_animation"
                )
            except Exception as e:
                st.image("https://cdn-icons-png.flaticon.com/512/4939/4939496.png", width=120)
    
    return (query, search_mode) if search_button and query else (None, None)