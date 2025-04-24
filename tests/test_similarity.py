from backend.similarity import find_similar_threads

results = find_similar_threads("Show me deep convos about AI ethics with humor")
for r in results:
    print(f"🧵 {r['title']}\n🔍 {r['tags']}\n📄 {r['content']}\n")

