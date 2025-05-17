def infer_subject(text):
    SUBJECT_KEYWORDS = {
        "Biology": ["photosynthesis", "cell", "organism"],
        "Physics": ["force", "acceleration", "gravity", "newton"],
        "Math": ["algebra", "equation", "integral"],
        "Chemistry": ["atom", "molecule", "reaction"],
        "History": ["war", "empire", "king"]
    }
    text = text.lower()
    for subject, keywords in SUBJECT_KEYWORDS.items():
        if any(word in text for word in keywords):
            return subject
    return "General"
