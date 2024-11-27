from django import forms

from main.models import Student

GENDER_CHOICES = {"Male": "Male", "Female": "Female"}
class StudentForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email','gender', 'dob']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'min': '1980-01-01', 'max': '2005-12-31'}),
        }

from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'instructor', 'start_date', 'end_date', 'is_active']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }