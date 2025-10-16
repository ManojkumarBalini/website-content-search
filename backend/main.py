from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.services.html_parser import HTMLParser
from app.services.vector_search import VectorSearch

app = FastAPI(title="Website Content Search API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchRequest(BaseModel):
    url: str
    query: str

class SearchResponse(BaseModel):
    results: list

html_parser = HTMLParser()
vector_search = VectorSearch()

@app.post("/search", response_model=SearchResponse)
async def search_website(request: SearchRequest):
    try:
        print(f"Fetching content from: {request.url}")
        html_content = html_parser.fetch_html(request.url)
        print("HTML content fetched successfully")
        
        chunks_data = html_parser.extract_structured_chunks(html_content)
        print(f"Created {len(chunks_data)} structured chunks")
        
        if not chunks_data:
            return SearchResponse(results=[])
        
        text_chunks = [chunk['text'] for chunk in chunks_data]
        search_results = vector_search.search_similar(text_chunks, request.query, top_k=20)
        
        unique_results = []
        seen_hashes = set()
        
        for result in search_results:
            for chunk_data in chunks_data:
                if chunk_data['text'] == result["content"]:
                    content_hash = chunk_data['content_hash']
                    
                    if content_hash not in seen_hashes:
                        seen_hashes.add(content_hash)
                        
                        display_content = ""
                        if chunk_data['heading']:
                            display_content += f"<strong>{chunk_data['heading']}</strong>"
                        if chunk_data['heading'] and chunk_data['paragraph']:
                            display_content += "<br/><br/>"
                        if chunk_data['paragraph']:
                            paragraph_lines = chunk_data['paragraph'].split('. ')
                            if len(paragraph_lines) > 3:
                                display_content += '. '.join(paragraph_lines[:3]) + '.'
                            else:
                                display_content += chunk_data['paragraph']
                        
                        unique_results.append({
                            "content": display_content,
                            "html_content": chunk_data['html'],
                            "match_score": round(result["score"] * 100),
                            "path": request.url,
                            "heading": chunk_data['heading'],
                            "paragraph": chunk_data['paragraph']
                        })
                        
                        if len(unique_results) >= 10:
                            break
                    break
            
            if len(unique_results) >= 10:
                break
        
        print(f"Returning {len(unique_results)} unique results")
        return SearchResponse(results=unique_results)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
