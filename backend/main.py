from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    # 连接到本地运行的Ollama服务
    response = requests.post('http://localhost:11434/api/generate', 
        json={
            "model": "llama2",
            "prompt": request.message
        }
    )
    
    return {"response": response.json()["response"]} 