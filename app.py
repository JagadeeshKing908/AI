from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class Request(BaseModel):
    prompt: str

@app.post("/chat")
def chat(request: Request):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": request.prompt}]
    )
    return {"response": response['choices'][0]['message']['content']}
