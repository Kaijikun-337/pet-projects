students = [
    {"id": 1, "name": "Aziza", "group": "Group A"},
    {"id": 2, "name": "Sardor", "group": None},      
    {"id": 3, "name": None, "group": "Group B"},      
    {"id": 4}                                         
]

# 1. Name the variable clearly (it's a 'student', not an 'index')
for student in students:
    
    # 2. EXTRACT SAFELY
    # .get("key") returns None if missing.
    # 'or "Unknown"' provides a backup if the result is None.
    name = student.get("name") or "Unknown Student"
    group = student.get("group") or "No Group"
    
    # 3. PRINT
    print(f"Student: {name} | Group: {group}")