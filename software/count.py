__author__ = 'abdullahfadel'
from django.template import Template, Context
from django.template.loader import get_template
from django.http import HttpResponse, Http404


def count_number_word(request):
    file =get_template('software.html').render()

    dict_count={}

    for word in file.split():
        if word not in  dict_count:
             dict_count[word] = 1
        else:
             dict_count[word] += 1

    for key,value in  dict_count.items():
        print key, value
    t=get_template('count_number.html')

    html = t.render(Context({'z': dict_count.items()}))

    return HttpResponse(html)






