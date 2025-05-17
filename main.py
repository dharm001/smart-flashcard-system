from fastapi import FastAPI
from pydantic import BaseModel
from app.subject_infer import infer_subject
from app.db import add_flashcard, get_flashcards

app = FastAPI()

class Flashcard(BaseModel):
    student_id: str
    question: str
    answer: str

@app.post("/flashcard")
def create_flashcard(card: Flashcard):
    subject = infer_subject(card.question)
    add_flashcard(card.student_id, card.question, card.answer, subject)
    return {"message": "Flashcard added successfully", "subject": subject}

@app.get("/get-subject")
def fetch_flashcards(student_id: str, limit: int = 5):
    return get_flashcards(student_id, limit)
