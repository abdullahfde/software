"""software URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url

from django.contrib import admin

from software import count
from software import views
from software import view1

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'histogram/', count.count_number_word),
    url(r'^add-teacher/$',views.add_teacher),
    url(r'^all-teacher/$',views.all_teacher),
    url(r'^addstudent/$',views.addstudent),
    url(r'^all-students/$',views.all_students),
    url(r'^addcourse/$',views.addcourses),
    url(r'^all-course/$',views.all_courses),
    url(r'^select_course/$',views.select),
    url(r'^all_course_student/(.*)/$',views.all_course),




]

