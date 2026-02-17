student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for name, score in student_scores.items():
    if score >= 91:
        student_grades[name] = "Outstanding"
    if score >= 81 and score <= 90:
        student_grades[name] = "Exceeds Expectations"
    if score >= 71 and score < 81:
        student_grades[name] = "Acceptable"
    if score <= 70:
        student_grades[name] = "Fail"
