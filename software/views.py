__author__ = 'abdullahfadel'

from software.forms import teacherForm,studentForm,courseForm,EnrollForm
from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.template import Context
from django.shortcuts import render_to_response
import datetime
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext
from models import teacher,student,course
def add_teacher(request):
    if request.method == 'POST':
        form = teacherForm(request.POST)

        if form.is_valid():
            a = teacher(first_name=form.cleaned_data["first_name"],
                       last_name=form.cleaned_data["last_name"],
                       email=form.cleaned_data["email"],
                        office_details=form.cleaned_data['office_details'],
                        phone=form.cleaned_data['phone'])

            a.save()
            return HttpResponseRedirect('/all-teacher/')






    else:
        form = teacherForm()

    return render_to_response('add-teacher.html', {'form': form}, RequestContext(request))
def addstudent(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            b=student(first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            email=form.cleaned_data["email"])
            b.save()
            return HttpResponseRedirect('/all-students/')
    else:
        form=studentForm()
    return render_to_response('addstudent.html', {'form': form}, RequestContext(request))




def addcourses(request):
    if request.method == 'POST':
        form = courseForm(request.POST)
        if form.is_valid():

            b=course(name=form.cleaned_data["name"],
            code=form.cleaned_data["code"],
            classroom=form.cleaned_data["classroom"])
            b.save()
            return  HttpResponseRedirect('/all-course/')
    else:
        form=courseForm()
    return render_to_response('addcourse.html', {'form': form}, RequestContext(request))











def all_teacher(request):
 return render_to_response('all_teacher.html',
 {'teacher_list': teacher.objects.all()})

def all_students(request):
 return render_to_response('all_students.html',
 {'student_list': student.objects.all()})

def all_courses(request):
 return render_to_response('all_course.html',
 {'course_list': course.objects.all()})
def all_new(request):
     return render_to_response('allnew.html',
                                {'course_list': course.objects.all()})


def select(request):
    if request.method=="POST":
        form = EnrollForm(request.POST)
        if form.is_valid():
            print form.cleaned_data["students1"]
            studentname = student.objects.get(first_name=form.cleaned_data["students1"])
            coursename= course.objects.get(name=form.cleaned_data["courses"])
            coursename.students.add( studentname)
            return HttpResponseRedirect("/all_course_student/"+form.courses.cleaned_data["courses"])

    form=EnrollForm()
    return render_to_response("enroll.html",
                              {"form":form},RequestContext(request))
def all_course(request,a):
    c = course.objects.get(name=a)
    return render_to_response("allenroll.html",
                              {"course_student_list":c.students.all()})


