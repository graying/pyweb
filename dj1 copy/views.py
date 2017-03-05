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
