from django.shortcuts import render, HttpResponse
from .models import Student

def insert_student(request):
    student = Student(name="Aparna", age=19, email="aparna@gmail.com")
    student = Student(name="Manju", age=19, email="manju@gmail.com")
    student = Student(name="prasanna", age=19, email="prasanna@gmail.com") 
    student.save()
    return HttpResponse("Student record added successfully!")
def student_list(request):
    students = Student.objects.all()
    return render(request, 'modelapp/student_list.html', {'students': students})
