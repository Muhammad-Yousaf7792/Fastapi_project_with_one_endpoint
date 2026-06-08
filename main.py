from fastapi import FastAPI
from pydantic import BaseModel
import re

# Create FastAPI application
app = FastAPI()


class TextRequest(BaseModel):
    """Request model for incoming text."""
    text: str


@app.post("/analyze")
def analyze_text(request: TextRequest) -> dict:
    
    input_text = request.text.strip()

    words = input_text.split()
    word_count = len(words)

    character_count = len(input_text)

    sentences = [
        sentence for sentence in re.split(r"[.!?]+", input_text)
        if sentence.strip()
    ]
    sentence_count = len(sentences)

    return {
        "word_count": word_count,
        "character_count": character_count,
        "sentence_count": sentence_count
    }