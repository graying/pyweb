from django import template
from django.http import HttpResponse
import datetime

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
    t = template.Template("this is a template named {{ temp_name }}.")
    c = template.Context({'temp_name': 'Eddys_Template'})
    return HttpResponse(t.render(c))
