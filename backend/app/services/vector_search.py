import re
import math
from collections import Counter

class VectorSearch:
    def __init__(self):
        pass
    
    def simple_similarity(self, chunks: list, query: str) -> list:
        if not chunks or not query:
            return []
        
        query_terms = set(re.findall(r'\w+', query.lower()))
        
        results = []
        
        for chunk in chunks:
            if not chunk:
                continue
                
            chunk_terms = re.findall(r'\w+', chunk.lower())
            if not chunk_terms:
                continue
            
            chunk_term_set = set(chunk_terms)
            chunk_term_freq = Counter(chunk_terms)
            
            # Calculate simple similarity score
            exact_matches = len(query_terms.intersection(chunk_term_set))
            
            # Calculate term frequency score
            tf_score = 0
            for term in query_terms:
                if term in chunk_term_freq:
                    tf_score += chunk_term_freq[term] / len(chunk_terms)
            
            # Combine scores
            similarity = exact_matches + tf_score
            
            # Bonus for exact phrase matches
            if query.lower() in chunk.lower():
                similarity += 5
                
            results.append({
                "content": chunk,
                "score": similarity
            })
        
        # Sort by similarity score and return top results
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:10]
    
    def search_similar(self, chunks: list, query: str, top_k: int = 10) -> list:
        return self.simple_similarity(chunks, query)
