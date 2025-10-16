from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class VectorSearch:
    def __init__(self):
        pass
    
    def search_similar(self, chunks: list, query: str, top_k: int = 10) -> list:
        if not chunks:
            return []
        
        try:
            documents = chunks + [query]
            vectorizer = TfidfVectorizer().fit(documents)
            vectors = vectorizer.transform(documents)
            
            query_vector = vectors[-1]
            chunk_vectors = vectors[:-1]
            
            similarities = cosine_similarity(query_vector, chunk_vectors).flatten()
            
            scored_chunks = list(zip(chunks, similarities))
            scored_chunks.sort(key=lambda x: x[1], reverse=True)
            
            top_results = scored_chunks[:top_k]
            
            return [
                {
                    "content": chunk,
                    "score": float(score)
                }
                for chunk, score in top_results
            ]
        except Exception as e:
            print(f"Vector search error: {e}")
            return []
