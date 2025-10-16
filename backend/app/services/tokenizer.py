import re

class Tokenizer:
    def __init__(self):
        pass
    
    def count_tokens(self, text: str) -> int:
        words = text.split()
        return len(words)
    
    def create_chunks(self, text: str, max_tokens: int = 500) -> list:
        if not text:
            return []
            
        sentences = re.split(r'[.!?]+', text)
        chunks = []
        current_chunk = ""
        current_token_count = 0
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
                
            sentence_tokens = self.count_tokens(sentence)
            
            if current_token_count + sentence_tokens <= max_tokens:
                if current_chunk:
                    current_chunk += ". " + sentence
                else:
                    current_chunk = sentence
                current_token_count += sentence_tokens
            else:
                if current_chunk:
                    chunks.append(current_chunk)
                current_chunk = sentence
                current_token_count = sentence_tokens
        
        if current_chunk:
            chunks.append(current_chunk)
        
        return chunks