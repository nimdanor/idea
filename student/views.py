
from django.http import HttpResponse,Http404
from django.shortcuts import get_object_or_404,get_list_or_404,render_to_response
from django.template import RequestContext, loader
from django.shortcuts import render
from student.models import Student
from concept.models import Concept


# Create your views here.


def students(request):
    template = loader.get_template("student/listS.html")
    context = RequestContext(request, {
        'image':  1,
        'list':get_list_or_404(Student),
    })

    return HttpResponse(template.render(context))


def chooseconcept(request,studid):
	S = get_object_or_404(Student,student_id=studid)
	template = loader.get_template("student/listC.html")
	context = RequestContext(request, {
		'image':  1,
		'stu':studid,
		'list':get_list_or_404(Concept),
	})
	return HttpResponse(template.render(context))

def stuaddconcept(request,student_id,concept_id,level):
	S = get_object_or_404(Student,student_id=student_id)
	C = get_object_or_404(Concept,pk=concept_id)
	S.addConcept(C.name,level)
	return chooseconcept(request,student_id)
