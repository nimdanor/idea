from django.db import models
import datetime
import json

# Create your models here.

def mynow():
#	tz = datetime.tzinfo("Europe/Paris")
	return datetime.datetime.now()

class Pldata(models.Model):
	stamp = models.DateTimeField("time",default=datetime.datetime.now, blank=True)
	data  = models.TextField("jsondata",default="{}")




def addnew(thedata):
	n = Pldata()
	n.data = thedata
	n.save()


