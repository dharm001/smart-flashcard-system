# Smart Flashcard Backend

A RESTful backend that classifies flashcards by subject using rule-based NLP and serves mixed-subject flashcards on request.

## 🔧 Installation

```bash
git clone https://github.com/YOUR_USERNAME/smart_flashcard.git
cd smart_flashcard
pip install -r requirements.txt
```

## 🚀 Running the Server

```bash
uvicorn app.main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📌 Endpoints

### 1. Add Flashcard
`POST /flashcard`

```json
{
  "student_id": "stu001",
  "question": "What is Newton's Second Law?",
  "answer": "Force equals mass times acceleration"
}
```

### 2. Get Mixed Flashcards
`GET /get-subject?student_id=stu001&limit=5`

### 📦 Example Response

```json
[
  {
    "question": "What is Newton's Second Law?",
    "answer": "Force equals mass times acceleration",
    "subject": "Physics"
  }
]
```

## ✅ How to Submit
1. Push this to your public GitHub repo
2. Test the API on localhost
3. Submit the GitHub link in the Google Form
