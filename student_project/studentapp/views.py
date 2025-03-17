from django.shortcuts import render

def student_list(request):
    students = [
        {'name': 'Alice', 'marks': 85},
        {'name': 'Bob', 'marks': 40},
        {'name': 'Charlie', 'marks': 75},
        {'name': 'David', 'marks': 90},
    ]
    passing_marks = 50  # Define passing marks threshold
    return render(request, 'students/student_list.html', {'students': students, 'passing_marks': passing_marks})
