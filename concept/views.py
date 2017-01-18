__author__ = 'dr'
from django.http import HttpResponse,Http404
from django.shortcuts import get_object_or_404,get_list_or_404,render_to_response
from concept.models import Concept,Link,getRoots,updateLevel,ConceptForm,AddLinkForm,toJson
from graphviz import Digraph
from django.template import RequestContext, loader
from django.core import serializers
from student.models import Student
from jsonview.decorators import json_view

def level(request):
    updateLevel()
    return graphRL(request)


@json_view
def jsonview(request):
	return toJson()


def debugview(request, concept_id):
	text = "debug view"
	student = get_object_or_404(Student,student_id=11)
	ci = get_object_or_404(Concept,pk=concept_id)
	text += student.addConceptIfLevel(ci.name,2)
	return HttpResponse(text)

def racine(request):
    return  default(request,concept_id=1)


def graph(request,rankdir):
    descl = []
    for r in getRoots():
        descl += r.getDescendantLinks()

    return makeGraph(request,descl,"graphe general","general",rankdir)

def small(request, student_num):
	descl = []
	for r in getRoots():
		descl += r.getDescendantLinks()

	dumpgraph(request,descl,"Graphe local PL","RL",student=student_num,ALL=False)

	template = loader.get_template("concept/graph_only.html")
	context = RequestContext(request, {
		'image':  2,
		'hidden':'fnum',
		'cname':"Graphe réduit"
	})
	return HttpResponse(template.render(context))

def onlyGraph(request,student_num):
	descl = []
	for r in getRoots():
		descl += r.getDescendantLinks()

	dumpgraph(request,descl,"Graphe Epistèmes PL","RL",student=student_num)

	template = loader.get_template("concept/graph_only.html")
	context = RequestContext(request, {
		'image':  2,
		'hidden':'fnum',
		'cname':"Graphe Complet"
	})
	return HttpResponse(template.render(context))



def nonzerograph(request,student_num):
	descl = []
	for r in getRoots():
		descl += r.getDescendantLinks()

	dumpgraph(request,descl,"Graphe Epistèmes PL","RL",student=student_num)

	template = loader.get_template("concept/graph_only.html")
	context = RequestContext(request, {
		'image':  2,
		'hidden':'fnum',
		'cname':"Graphe Complet"
	})
	return HttpResponse(template.render(context))


def knowls(request,concept_id):
    r = get_object_or_404(Concept,pk=concept_id)
    text = "<div><p>" +  r.description + "</p></div>"
    return HttpResponse(text)

def dumpgraph(request,descl, comment,rankdir="RL", student=None,ALL=True):
	dot = Digraph(comment=comment)
	dot.format='svg'
	dot.graph_attr['rankdir'] = rankdir
	if student != None:
		student = get_object_or_404(Student,student_id=student)

	s=set()
	for l in descl:
		s.add(l.ascendant)
		s.add(l.descendant)
	for x in s:
		if student != None and student.knowsConcept(x.name) :
			cc = student.conceptlevel(x.name)
			l= ['red','green','orange','yellow']
			cc=l[min(cc,len(l)-1)]
			dot.node(x.name,URL=x.makeUrl(),color=cc,style="filled",shape="box")
		else:
			if ALL :
				dot.node(x.name,URL=x.makeUrl(),color="red",style="filled",shape="box")

	for l in descl:
		if ALL:
			dot.edge(l.descendant.name,l.ascendant.name)
		else:
			if student != None and student.knowsConcept(l.descendant.name) and student.knowsConcept(l.ascendant.name):
				dot.edge(l.descendant.name,l.ascendant.name)
	dot.render('concept/templates/concept/graph')

def makeGraph(request,descl,comment , cname,rankdir="RL"):
	dumpgraph(request,descl,comment,rankdir)

	template = loader.get_template("concept/graph.html")
	context = RequestContext(request, {
		'image':  2,
		'hidden':'fnum',
		'cname':cname
	})
	return HttpResponse(template.render(context))




def graphRL(request):
    return graph(request,'RL')

def graphTB(request):
    return graph(request,'TB')

def graphLR(request):
    return graph(request,'LR')

def graphBT(request):
    return graph(request,'BT')


def graphTT(request,concept_id):
    r = get_object_or_404(Concept,pk=concept_id)

    comment = "graphe de concept du concept "+r.name

    descl = r.getDescendantLinks()
    return makeGraph(request,descl,comment,r.name)


def listing(request):
    template = loader.get_template("concept/listing.html")
    context = RequestContext(request, {
        'image':  1,
        'list':get_list_or_404(Concept),
    })

    return HttpResponse(template.render(context))


def create(request):
    if request.method == 'POST':
        print("POST")
        form = ConceptForm(request.POST,instance=Concept())
        if form.is_valid():
                form.save()
                return listing(request)

        return render_to_response('concept/create.html', {'theform' : form, 'image':  1, 'etat':'invalide' },context_instance=RequestContext(request))

    elif request.method == 'GET':
        form = ConceptForm(instance=Concept())
        return render_to_response('concept/create.html', {'theform' : form, 'image':  1,'etat':'valide' },context_instance=RequestContext(request))


def edit(request,concept_id):
    r=get_object_or_404(Concept,pk=concept_id)
    if request.method == 'POST':
        print("POST")
        form = ConceptForm(request.POST,instance=r)
        if form.is_valid():
                form.save()
                l=list()
                l.append(get_object_or_404(Concept,pk=concept_id))
                template = loader.get_template("concept/listing.html")
                context = RequestContext(request, {
                        'image':  1,
                        'list': l,
                    })
                return HttpResponse(template.render(context))
        else:
             return  graphLR(request)
    elif request.method == 'GET':
        form = ConceptForm(instance=r)
        return render_to_response('concept/edit.html', {'theform' : form, 'image':  1, },context_instance=RequestContext(request))
    else:
        return graphTB(request)

def export(request,type):
    # utilisation d'un sérialiseur json
    # question comment le lier a une réponse Http
    # ou est le flus correspondant
        return graphTB(request)

import pdb


def dotheMagic(c1,c2):
   nl = Link(descendant=c2,ascendant=c1)
   nl.save()

def addPreLink(request,concept_id):
    '''
    Objectif ajouter un lien entre un prérequis et le concept concept_id
    :param concept_id le concept qui va aquérir un nouveau prérequis
    :return:
    '''
    r=get_object_or_404(Concept,pk=concept_id)
    if r.pk == 1:
        return render_to_response('concept/racine.html',{ 'image':  1, },context_instance=RequestContext(request))
    if request.method == 'GET':
        l = r.getNietherAscendantNorDescendant()

        theList = [ (o.pk, o.name+"("+o.lname+")") for o in l ]
        form = AddLinkForm(theList)
        return render_to_response('concept/linkedit.html', {'theform' : form, 'concept': r, },context_instance=RequestContext(request))
    elif request.method == 'POST':
        theInitiaList = [ str(o.pk) for o in r.getAscendant() ]
        for k in request.POST.getlist('prerequis'):
            if not k in theInitiaList:
                dotheMagic(get_object_or_404(Concept,pk=k),get_object_or_404(Concept,pk=r.pk))

        return graphTB(request)

    else:
        # il faut sauvegarder les liens clickés
        return graphTB(request)
