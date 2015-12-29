__author__ = 'abdullahfadel'
from django import forms
from software.models import student
from software.models import course
class teacherForm(forms.Form):
     first_name=forms.CharField(max_length=40)
     last_name=forms.CharField(max_length=30)
     office_details=forms.CharField(max_length=70)
     phone=forms.CharField(max_length=20)
     email=forms.EmailField()
class studentForm(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=40)
    email=forms.EmailField()
class courseForm(forms.Form):
    name=forms.CharField(max_length=30)
    code=forms.CharField(max_length=50)
    classroom=forms.CharField(max_length=60)
courses = [(cours.name,cours.name) for cours in course.objects.all()]

students = [(students.first_name,students.first_name) for students in student.objects.all()]

class EnrollForm(forms.Form):
    courses = forms.ChoiceField(courses, required=False,widget=forms.Select())
    students1 =forms.ChoiceField(students,required=False,widget=forms.Select())





