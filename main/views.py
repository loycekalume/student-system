from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.models import Student, Enrollment


# Create your views here.
def students(request):
    students = Student.objects.all()  # select * from students
    return render(request, 'students.html', {"students": students})


# def test(request):


# s1 = Student(first_name='John',last_name='Smith', email='john@gmail.com', gender='male', dob='2003-01-28')
# s1.save()
#
# s1 = Student(first_name='Miles', last_name='Smith', email='miles@gmail.com', gender='male', dob='2002-01-28')
# s1.save()
#
# students = Student.objects.count()
# s1 = Student.objects.get(id=1)
# print(s1)
# enrollments = Enrollment.objects.count()
# enrol = Enrollment(student=s1,grade=99)
# enrol.save()
#
# return HttpResponse(f"We have {students}  and {enrollments} saved")
def courses(request):
    return render(request, 'courses.html')


def enrollment(request):
    return render(request, 'enrollment.html')


def delete_student(request,student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect("students")