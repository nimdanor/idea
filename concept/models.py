from django.db import models
# wharning must be set in setting from django_ace import AceWidget
from django.shortcuts import get_object_or_404
from django.forms import Form, MultipleChoiceField, ModelForm, CheckboxSelectMultiple,Textarea
from django.forms.fields import ChoiceField,CharField
from concept.LowerCharField import LowerCaseCharField

from concept.exceptions import *

import json

# Create your models here.

class Concept(models.Model):
	"""
	Most important Class in the project
	This class stores concepts (see reference DRevuz [1] Concept in the project for more information ).
	"""
	# TODO : names must be in lowercase see file LowerCharField.py in this directory
	name = LowerCaseCharField("Le nom du concept", max_length=30, unique=True)  # nom du concept pour référence
	lname = models.CharField("Long Name", max_length=300, blank=True)  # nom plus complet pour désembiguisation
	description = models.TextField("Description")  # Description textuelle avec des exemples si nécessaire
	link = models.ManyToManyField('self', through='Link', symmetrical=False)  # un lien vers un autre concept nécessaire
	# other_concept = models.ManyToManyField('self',blank=True)  # un lien vers d'autres concepts nécessaire

	pub_date = models.DateTimeField('date created', auto_now_add=True)  # creation time
	update = models.DateTimeField('date update', auto_now=True)  #
	level = models.IntegerField('niveau', default=-1)



	def racine():
		return Concept.objects.filter(pk=1)[0]


	def getDescendantNames(self):
		li=[]
		for u in self.getDescendant():
			li.append(u.name)
		return li

	def getAscendantNames(self):
		li=[]
		for u in self.getAscendant():
			li.append(u.name)
		return li


	def getDescendant(self):
		s1 = set(Link.objects.filter(name="prerequisite", ascendant=self))
		s2 = set()
		for l in s1:
			s2.add(l.descendant)
		for u in s1:
			s2 = s2.union(u.descendant.getDescendant())

		return s2

	def getDescendantLinks(self):
		s1 = set(Link.objects.filter(name="prerequisite", ascendant=self))
		s2 = set()
		for l in s1:
			s2.add(l)
		for u in s1:
			s2 = s2.union(u.descendant.getDescendantLinks())
		return s2


	def getAscendant(self):
		s1 = set(Link.objects.filter(name="prerequisite", descendant=self))
		s2 = set()
		for l in s1:
			s2.add(l.ascendant)
		for u in s1:
			s2 = s2.union(u.ascendant.getAscendant())
		return s2

	def getNotDescendant(self):
		s1 = self.getDescendant()
		all = list(Concept.objects.all())
		s2 = set()
		for c in all:
			if not c in s1 and c != self:
				s2.add(c)
		return s2

	def getNietherAscendantNorDescendant(self):
		s1 = self.getDescendant()
		s2 = self.getAscendant()
		all = set(Concept.objects.exclude(pk=self.pk).all())
		r = (all - s1) - s2
		return r

	def __unicode__(self):
		return u'%s' % (self.name)

	def __str__(self):
		return r'%s' % (self.name)

	def save(self, *args, **kwargs):
		super(Concept, self).save(*args, **kwargs)  # Call the "real" save() method.
		if self.pk != 1:
			racine = get_object_or_404(Concept, pk=1)
			l = Link(name="prerequisite", descendant=self, ascendant=racine)
			l.save()

	def delete(self):
		# si c'est la racine ne pas effacer
		print("delete self pk =", self.pk)
		if self.pk == 1 or self.name == "racine":
			return

		# faire la liste des predesceseur de self
		pred = [o.ascendant for o in Link.objects.filter(ascendant=self)]
		# faire la liste des sucesseur de self
		succ = [o.descendant for o in Link.objects.filter(descendant=self)]
		#super(Concept,self).delete()
		# creer un lien de
		super(Concept, self)

	def makeLabel(self):
		bob = self.name + " " + str(self.level) + " " + str(self.pk) + " "
		return bob


	def makeUrl(self):
		return "/concept/edit/" + str(self.pk)


	def dolevelupdate(self, level):

		self.level = level
		self.save()

		s1 = set(Link.objects.filter(name="prerequisite", ascendant=self))
		for c in s1:
			c.descendant.dolevelupdate(level + 1)


def toJson():
	s="["
	for cc in Concept.objects.all():

		s += "{  \"name\":\"" +str(cc.name)+ "\","
		s += "  \"lname\":\"" +str(cc.lname)+ "\","
		s += "  \"description\": " + json.dumps(cc.description)+ "},"
	s += "]"
	return s



class Link(models.Model):
    name = models.CharField("Le type du lien", max_length=30, default="prerequisite")
    ascendant = models.ForeignKey(Concept, related_name='prerequis')
    descendant = models.ForeignKey(Concept, related_name='element')

    def save(self, *args, **kwargs):
        if self.name != "prerequisite":
            # pas de règles pour les liens d'un autre type
            super(Link, self).save(*args, **kwargs)
            return
        if self.descendant == self.ascendant:
            return CreateCycleException(self.ascendant, self.ascendant, "anti-symetric")
        if Link.objects.filter(name="prerequisite", descendant=self.descendant, ascendant=self.ascendant).count() == 1:
            return  # il y est déja
        if Link.objects.filter(name="prerequisite", descendant=self.ascendant, ascendant=self.descendant).count() == 1:
            raise CreateCycleException(self.descendant, self.ascendant, "direct")
        print(self.descendant.getDescendant())
        if self.ascendant in self.descendant.getDescendant():
            # si la relation inverse existe faire échec à la création
            raise CreateCycleException(self.descendant, self.ascendant, "indirect")
        if self.ascendant in self.descendant.getAscendant():
            # si la relation  existe par cloture transitive ne rien faire
            return

        super(Link, self).save(*args, **kwargs)  # Call the "real" save() method.
        # il faut retirer tout les liens de dependance entre ascendant et les descendant de descendant
        #
        lesdesc = self.descendant.getDescendant()
        ascdesc = self.ascendant.getAscendant()
        ascdesc.add(self.ascendant)
        lesdesc.add(self.descendant)
        for asc in ascdesc:
            for des in lesdesc:
                print("checking " + asc.name + "   " + des.name)
                if asc == self.ascendant and des == self.descendant:
                    print("seeing self")
                else:
                    Link.objects.filter(name="prerequisite", ascendant=asc, descendant=des).delete()

    def delete(self, using):
        print("using delete :" + using)
        super(Link, self).delete(using)  # Call the "real" delete() method.
        print("after delete ")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


    def __unicode__(self):
        return u'(%s->%s)' % (self.ascendant.name, self.descendant.name)


def getRoots():
    """
    the list of roots is the list of Concept root such Link.objects.filter(descendant=root).count() ==0
    :return: the list of roots
    """
    ret = []
    for cc in Concept.objects.all():
        if Link.objects.filter(descendant=cc).count() == 0:
            ret.append(cc)
    return ret


def updateLevel():
    l = getRoots()
    for c in l:
        pass
        c.dolevelupdate(0)


class ConceptForm(ModelForm):
    #description = CharField(widget=AceWidget)
    class Meta:
        model = Concept
        fields = (
            'name',  # nom du concept pour référence
            'lname',  # nom plus complet pour désembiguisation
            'description',  # Description textuelle avec des exemples si nécessaire
        )


class AddLinkForm(Form):
    # il faut la liste de tout les concepts qui de sont pas des descendant du concept courrant
    def __init__(self, theList, *args, **kwargs):
        super().__init__()
        if isinstance(theList, list):
            self.fields['prerequis'] = MultipleChoiceField(required=True, widget=CheckboxSelectMultiple,
                                                           choices=theList)

