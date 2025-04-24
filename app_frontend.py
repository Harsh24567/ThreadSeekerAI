import streamlit as st
import requests

st.set_page_config(page_title="ThreadSeekerAI", layout="wide")

st.title("🧵 ThreadSeekerAI")
st.subheader("Discover threads that match your vibe, instantly ✨")

query = st.text_input("🔍 What are you looking for?", placeholder="e.g. AI ethics with humor")

if st.button("Search") and query:
    with st.spinner("Thinking like an AI..."):
        try:
            res = requests.post(
                "http://127.0.0.1:5000/search",
                json={"query": query}
            )
            data = res.json()

            if "results" in data:
                for i, thread in enumerate(data["results"], 1):
                    st.markdown(f"### {i}. {thread['title']}")
                    st.write(thread["content"])
                    st.caption(f"Tags: {', '.join(thread['tags'])}")
                    st.markdown("---")
            else:
                st.error(data.get("error", "Something went wrong."))

        except Exception as e:
            st.error(f"API Error: {e}")

