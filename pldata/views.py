from django.shortcuts import render,HttpResponse
from pldata.models import addnew,Pldata
# Create your views here.

import json

def addnewdata(request):
	if request.method != 'GET':
		return HttpResponse("error pas GET")
	try:
		json.loads((request.body.decode("utf-8") ))

		addnew(request.body.decode("utf-8"))

		# TODO save to bvase
		return HttpResponse("OK") # TODO renvoyer ok 200
	except Exception as e:
		return HttpResponse("JSON Mal Formé: {}   {}".format(request.body,e)) # TODO ERRO 500

def viewsdata(request):
	s=""
	for cc in Pldata.objects.all():
		s += str(cc.data)
		s += "<br>"
	return HttpResponse(s)


