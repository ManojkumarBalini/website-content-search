import re
from collections import Counter
import math

class VectorSearch:
    def __init__(self):
        pass
    
    def tf_idf_similarity(self, chunks: list, query: str) -> list:
        if not chunks:
            return []
        
        # Tokenize query
        query_terms = set(re.findall(r'\w+', query.lower()))
        
        # Calculate TF-IDF scores
        results = []
        
        # Calculate document frequency for IDF
        doc_freq = Counter()
        for chunk in chunks:
            chunk_terms = set(re.findall(r'\w+', chunk.lower()))
            doc_freq.update(chunk_terms)
        
        total_docs = len(chunks)
        
        for chunk in chunks:
            chunk_terms = re.findall(r'\w+', chunk.lower())
            chunk_term_freq = Counter(chunk_terms)
            
            similarity = 0
            for term in query_terms:
                if term in chunk_term_freq:
                    # TF (term frequency in this chunk)
                    tf = chunk_term_freq[term] / len(chunk_terms)
                    
                    # IDF (inverse document frequency)
                    idf = math.log((total_docs + 1) / (doc_freq[term] + 1)) + 1
                    
                    similarity += tf * idf
            
            # Also consider exact matches and partial matches
            exact_matches = len(query_terms.intersection(set(chunk_terms)))
            similarity += exact_matches * 0.5
            
            results.append({
                "content": chunk,
                "score": similarity
            })
        
        # Sort by similarity score
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:10]
    
    def search_similar(self, chunks: list, query: str, top_k: int = 10) -> list:
        return self.tf_idf_similarity(chunks, query)
