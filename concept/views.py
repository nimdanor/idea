__author__ = 'dr'
from django.http import HttpResponse,Http404
from django.shortcuts import get_object_or_404,get_list_or_404,render_to_response
from concept.models import Concept,Link,getRoots,updateLevel,ConceptForm,AddLinkForm
from graphviz import Digraph
from django.template import RequestContext, loader
from django.core import serializers


def level(request):
    updateLevel()
    return graphRL(request)




def racine(request):
    return  default(request,concept_id=1)


def graph(request,rankdir):
    descl = []
    for r in getRoots():
        descl += r.getDescendantLinks()

    return makeGraph(request,descl,"graphe general","general",rankdir)




def makeGraph(request,descl,comment , cname,rankdir="RL"):

    dot = Digraph(comment=comment)
    dot.format='svg'
    dot.graph_attr['rankdir'] = rankdir
    s=set()
    for l in descl:
        s.add(l.ascendant)
        s.add(l.descendant)
    for x in s:
        dot.node(x.name,URL=x.makeUrl())
        dot.node(x.name,URL=x.makeUrl())
    for l in descl:
        dot.edge(l.descendant.name,l.ascendant.name)
    dot.render('concept/templates/concept/graph')

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
    # utilisation d'un sérialiseur
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