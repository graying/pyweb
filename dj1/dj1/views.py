import datetime, os

from django import template
from django.http import HttpResponse
from django.template.loader import get_template

def index(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s  :</td><td>%s</td><br/><tr>' % (k,v))
    return HttpResponse(html)

def hello(request):
    return HttpResponse("Hello world!......")


def date_time(request):
    now = datetime.datetime.now()
    html = "<html><body>Haha! It is now %s.</body></html>" % now
    return HttpResponse(html)


def smile(request):
    html = "<html><h1>Haha! smile</h1></html>"
    return HttpResponse(html)


def t1test(request):
    t = get_template("t1test.html")
    name_set = ["Eddy", "Hugo", "Edison"]
    c = template.Context({'temp_name': 'Eddys_Template', 'number': '12', 'name_set': name_set})

    return HttpResponse(t.render(c))
