from sentence_transformers import SentenceTransformer, util
import json
import torch

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_threads(file_path="thread_data.json"):
    with open(file_path, 'r') as f:
        return json.load(f)

def find_similar_threads(query, top_k=3):
    threads = load_threads()
    contents = [thread['content'] for thread in threads]
    
    query_embedding = model.encode(query, convert_to_tensor=True)
    content_embeddings = model.encode(contents, convert_to_tensor=True)

    similarities = util.pytorch_cos_sim(query_embedding, content_embeddings)[0]
    top_indices = torch.topk(similarities, k=top_k).indices

    return [threads[i] for i in top_indices]

