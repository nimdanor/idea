from django.db import models
from collections import deque
from  concept.exceptions import *
# Create your models here.

class Concept(models.Model):
    '''
    Most important Class in the project
    This class stores concepts (see reference DRevuz [1] Concept in the project for more information ).
    '''
    # TODO : uniquement des identifiants en minuscule pour le name_concept
    name  = models.CharField("Le nom du concept", max_length=30,unique=True)  # nom du concept pour référence
    lname = models.CharField("Long Name", max_length=300, blank=True)  # nom plus complet pour désembiguisation
    description = models.TextField("Description")  # Description textuelle avec des exemples si nécessaire
    link = models.ManyToManyField('self',through='Link',symmetrical=False)  # un lien vers un autre concept nécessaire
    #other_concept = models.ManyToManyField('self',blank=True)  # un lien vers d'autres concepts nécessaire

    pub_date = models.DateTimeField('date created', auto_now_add=True)  # creation time
    update = models.DateTimeField('date update', auto_now=True)  #
    level = models.IntegerField('niveau',default=-1)

    def  getDescendant(self):
        s1 = set(Link.objects.filter(ascendant=self))
        s2=set()
        for l in s1:
            s2.add(l.descendant)
        for u in s1 :
             s2= s2.union(u.descendant.getDescendant())

        return s2

    def getAscendant(self):
        pass

    def __unicode__(self):
        return u'%s' % (self.name)
    def __str__(self):
        return r'%s' % (self.name)



class Link(models.Model):
    name = models.CharField("Le type du lien", max_length=30,default="prerequisite")
    ascendant = models.ForeignKey(Concept,related_name='from')
    descendant = models.ForeignKey(Concept,related_name='to')

    def save(self, *args, **kwargs):
        if Link.objects.filter(descendant=self.descendant, ascendant=self.ascendant).count() == 1:
                return # il y est déja
        if Link.objects.filter(descendant=self.ascendant, ascendant=self.descendant).count() == 1:
            raise CreateCycleException(self.descendant,self.ascendant,"direct")
        print(self.descendant.getDescendant())
        if self.ascendant in self.descendant.getDescendant():
            raise CreateCycleException(self.descendant,self.ascendant,"indirect")
        # si la relation inverse existe faire échec à la création
        # if Link.objects.filter()
        #if self.create_cycle():   # if adding this lien would create a cycle Don't do it
        #     return "Cycle"
        # else:
        super(Link, self).save(*args, **kwargs) # Call the "real" save() method.
        # il faut retirer tout les liens de dependance entre ascendant et les descendant de descendant

    def __unicode__(self):
        return u'(%s->%s)' % (self.ascendant.name,self.descendant.name)