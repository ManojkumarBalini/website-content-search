import requests
from bs4 import BeautifulSoup
import hashlib

class HTMLParser:
    def fetch_html(self, url: str) -> str:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, timeout=10, headers=headers)
            response.raise_for_status()
            return response.text
        except Exception as e:
            raise Exception(f"Failed to fetch URL: {str(e)}")

    def extract_structured_chunks(self, html: str) -> list:
        soup = BeautifulSoup(html, 'html.parser')
        
        for script in soup(["script", "style"]):
            script.decompose()
        
        chunks = []
        seen_content = set()
        
        content_containers = soup.find_all(['div', 'section', 'article'], class_=True)
        
        for container in content_containers:
            headings = container.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            paragraphs = container.find_all('p')
            
            if headings and paragraphs:
                for heading in headings:
                    heading_text = heading.get_text(strip=True)
                    if not heading_text:
                        continue
                    
                    next_p = heading.find_next('p')
                    if next_p:
                        paragraph_text = next_p.get_text(strip=True)
                        if paragraph_text and len(paragraph_text) > 30:
                            content_hash = hashlib.md5(f"{heading_text}{paragraph_text}".encode()).hexdigest()
                            
                            if content_hash not in seen_content:
                                seen_content.add(content_hash)
                                
                                chunk_text = f"{heading_text} {paragraph_text}"
                                
                                chunk_html = f"""
<div class="{' '.join(container.get('class', []))}">
    {str(heading)}
    {str(next_p)}
</div>
                                """.strip()
                                
                                chunks.append({
                                    'text': chunk_text,
                                    'html': chunk_html,
                                    'heading': heading_text,
                                    'paragraph': paragraph_text,
                                    'content_hash': content_hash
                                })
        
        if not chunks:
            content_elements = soup.find_all(['div', 'section', 'article'])
            for element in content_elements:
                headings = element.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
                paragraphs = element.find_all('p')
                
                if headings and paragraphs:
                    for heading in headings:
                        heading_text = heading.get_text(strip=True)
                        if not heading_text:
                            continue
                        
                        for p in paragraphs:
                            paragraph_text = p.get_text(strip=True)
                            if paragraph_text and len(paragraph_text) > 30:
                                content_hash = hashlib.md5(f"{heading_text}{paragraph_text}".encode()).hexdigest()
                                
                                if content_hash not in seen_content:
                                    seen_content.add(content_hash)
                                    
                                    chunk_text = f"{heading_text} {paragraph_text}"
                                    chunk_html = f"""
<div>
    {str(heading)}
    {str(p)}
</div>
                                    """.strip()
                                    
                                    chunks.append({
                                        'text': chunk_text,
                                        'html': chunk_html,
                                        'heading': heading_text,
                                        'paragraph': paragraph_text,
                                        'content_hash': content_hash
                                    })
        
        return chunks[:20]