from django.http import HttpResponse
from datetime import datetime
from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    now = datetime.now()
    i = int(now.minute) % 3
    template = loader.get_template("acceuil.html")
    context = RequestContext(request, {
        'ima':  i,
    })
    return HttpResponse(template.render(context))

def acceuil(request):
    now = datetime.now()
    i = int(now.minute) % 3
    template = loader.get_template("acceuil.html")
    context = RequestContext(request, {
        'brout':  i,
    })
    return HttpResponse(template.render(context))


