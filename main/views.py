from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from main.app_form import StudentForm, CourseForm
from main.models import Student, Enrollment, Course


# Create your views here.
def students(request):
    students = Student.objects.all().order_by('-id').values()  # select * from students
    return render(request, 'students.html', {"students": students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Student {form.cleaned_data['first_name']} was added!")
            return redirect('students')
    form = StudentForm()
    return render(request,'student_form.html',{'form':form})





def enrollment(request):
    return render(request, 'enrollment.html')


def delete_student(request,student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect("students")

def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f"Student {form.cleaned_data['first_name']} was updated!")
            return redirect('students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_update_form.html', {"form": form})



def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

# Add a new course
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully!")
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})

# Edit an existing course
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, f"Course '{course.name}' updated successfully!")
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_edit_form.html', {'form': form})

# Delete a course
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    messages.success(request, f"Course '{course.name}' deleted successfully!")
    return redirect('course_list')


def enrollments(request):
    return None