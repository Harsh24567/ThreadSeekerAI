from backend.similarity import find_similar_threads

query = "Show me deep convos about AI ethics with humor"
results = find_similar_threads(query)

for idx, r in enumerate(results, start=1):
    print(f"Result {idx}:")
    print(f"🧵 Title: {r['title']}")
    print(f"📄 Content: {r['content']}")
    print(f"🏷️ Tags: {r['tags']}")
    print("="*50)

