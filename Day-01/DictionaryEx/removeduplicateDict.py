student_data = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    }
}

result = {}

for key, value in student_data.items():
    # Check if the current 'value' (student record) is not already in the 'result' dictionary.
    if value not in result.values():
        # If the 'value' is not already in 'result', add it to 'result' with its corresponding 'key'.
        result[key] = value

print(result) 
