from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_init, pre_save
from django.shortcuts import get_object_or_404
import json

class Student(models.Model):
	student_id = models.IntegerField(unique=True,)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	conceptjson = models.TextField(default='{"root":0}') #  the root concept known at level zero is the start for every one ;)


	def __str__(self):
		return "%d %s %s %s %s" % (self.student_id,self.first_name,self.last_name,self.conceptjson,self.conceptmap)

	def presave(self):
		print("pre self %s %s" % (self.conceptjson,self.conceptmap))
		self.conceptjson = json.dumps(self.conceptmap)

	def postload(self):
		self.conceptmap = json.loads(self.conceptjson)

	def addConcept(self,name,value):
		self.conceptmap = json.loads(self.conceptjson)
		print(self.conceptmap)
		self.conceptmap[name]=value
		self.save()

	def addConceptIfLevel(self,name,level):
		""""
		Sets the concept level if the level of the prerisites is equal or supperior to the level.
		"""
		c = get_object_or_404(Concept,name=name)
		for ac in c.getDescendant():
			if ac.name in self.conceptmap: # il existe
				if self.conceptmap[ac.name] < level:
					return "prérequis non maitrisé "+ac.name
			else:
				self.conceptmap[ac.name]=0
				return "prérequis non connu "+ac.name
		self.conceptmap[name]=level
		self.save()
		return "done"+str(self.conceptjson)

	def knowsConcept(self,name):
		return name in self.conceptmap

@receiver(post_init,sender=Student)
def post_my_callback(sender, **kwargs):
    # Your specific logic here
    #sender.postload()
	kwargs['instance'].conceptmap = dict() # this is an over kill is it ?
	kwargs['instance'].postload()
    #print("post (%s,%s)"  % (sender.conceptjson,sender.conceptmap))
	pass

@receiver(pre_save, sender=Student)
def pre_my_callback(sender, **kwargs):
	kwargs['instance'].presave()




