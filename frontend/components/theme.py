import streamlit as st

def setup_page():
    """Configure page theme and settings"""
    
    # Set page config
    st.set_page_config(
        page_title="ThreadSeekerAI",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        :root {
            --primary-color: #6366f1;
            --primary-light: #818cf8;
            --primary-dark: #4f46e5;
            --secondary-color: #f43f5e;
            --background-color: #f9fafb;
            --text-color: #1f2937;
            --text-light: #6b7280;
            --card-background: #ffffff;
            --border-radius: 12px;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }
        
        * {
            font-family: 'Inter', sans-serif;
        }
        
        .stApp {
            background: var(--background-color);
        }
        
        .main-title {
            background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 0;
            text-align: center;
        }
        
        .subtitle {
            color: var(--text-light);
            font-size: 1.1rem;
            text-align: center;
            margin-top: 0;
            margin-bottom: 2rem;
        }
        
        .header-container {
            margin-bottom: 2rem;
            padding-top: 1rem;
        }
        
        /* Form styling */
        div[data-testid="stForm"] {
            background: white;
            padding: 1.5rem;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-md);
            border: 1px solid rgba(0,0,0,0.05);
        }
        
        div.stRadio > div {
            display: flex;
            gap: 0.5rem;
        }
        
        div.stRadio label {
            cursor: pointer;
            background: white;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            display: flex !important;
            align-items: center;
            justify-content: center;
            box-shadow: var(--shadow-sm);
            border: 1px solid rgba(0,0,0,0.1);
            transition: all 0.2s;
        }
        
        div.stRadio label:hover {
            background: #f3f4f6;
        }
        
        /* Button styling */
        button[data-testid="baseButton-primary"] {
            background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 100%);
            border: none;
            padding: 0.6rem 1.5rem;
            border-radius: 8px;
            font-weight: 600;
            letter-spacing: 0.01em;
            box-shadow: 0 2px 8px rgba(99, 102, 241, 0.25);
            transition: all 0.2s;
        }
        
        button[data-testid="baseButton-primary"]:hover {
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
            transform: translateY(-1px);
        }
        
        /* Input styling */
        input[type="text"] {
            border-radius: 8px;
            padding: 0.75rem 1rem;
            border: 1px solid rgba(0,0,0,0.1);
            box-shadow: var(--shadow-sm);
            font-size: 1rem;
        }
        
        input[type="text"]:focus {
            border-color: var(--primary-color);
            box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2);
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .main-title {
                font-size: 2.2rem;
            }
            
            .subtitle {
                font-size: 1rem;
            }
            
            div[data-testid="stForm"] {
                padding: 1rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)