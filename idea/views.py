from django.http import HttpResponse,Http404
from datetime import datetime
from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    return acceuil(request,name="acceuil")

def acceuil(request,name):

    try:
        template = loader.get_template(name+".html")
    except:
        template = loader.get_template("acceuil.html")

    context = RequestContext(request, {
        'image': (int(datetime.now().minute) % 3),
        'hidden': name,
    })
    return HttpResponse(template.render(context))


def fnum(request,num):
    template = loader.get_template("acceuil.html")
    context = RequestContext(request, {
        'image':  num,
        'hidden':'fnum'
    })
    return HttpResponse(template.render(context))

