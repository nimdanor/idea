__author__ = 'dr'
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from concept.models import Concept,Link


def default(request,concept_id):
    c1= get_object_or_404(Concept,pk=concept_id)
    bob= c1.getDescendant()
    stri= "<html><body>TODO {{ %d %s %s }}</body></html>".format(int(concept_id),c1.name,bob)
    return  HttpResponse(stri)




def racine(request):
    return  default(request,concept_id=1)
