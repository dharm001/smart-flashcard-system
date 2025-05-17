import sqlite3
import random

conn = sqlite3.connect("flashcards.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS flashcards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT,
    question TEXT,
    answer TEXT,
    subject TEXT
)
""")
conn.commit()

def add_flashcard(student_id, question, answer, subject):
    cursor.execute(
        'INSERT INTO flashcards (student_id, question, answer, subject) VALUES (?, ?, ?, ?)',
        (student_id, question, answer, subject)
    )
    conn.commit()

def get_flashcards(student_id, limit):
    cursor.execute('SELECT question, answer, subject FROM flashcards WHERE student_id=?', (student_id,))
    results = cursor.fetchall()
    random.shuffle(results)
    seen_subjects = set()
    mixed = []
    for r in results:
        if r[2] not in seen_subjects:
            mixed.append({
                "question": r[0],
                "answer": r[1],
                "subject": r[2]
            })
            seen_subjects.add(r[2])
        if len(mixed) >= limit:
            break
    return mixed
