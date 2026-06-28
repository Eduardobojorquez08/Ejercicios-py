
students = {
    "Ana": 85,
    "Carlos": 62,
    "Maria": 91,
    "Luis": 74,
    "Sofia": 58,
    "Pedro": 88
}

def get_approved(students):
    approved_students = []
    for name, grade in students.items():
        if grade >= 70:
            approved_students.append(name)
        
    return approved_students
print(get_approved(students))
    