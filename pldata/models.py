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
	serverId = models.CharField("serveur",max_length=500)
	START="ST"
	TRY="TR"
	DONE="DN"
	STATEVALUES = ((START,"starting"), (TRY,"try"), (DONE,"done"))
	state = models.CharField(max_lenght=2,choices=STATEVALUES,default=TRY,editable=False)
	studentCode = models.TextField("studentcode",default="No code ?",editable=False)
	studentId = models.IntegerField("User Id",editable=False)

class Exercise(models.Model):
	author = models.CharField("author",max_length=300)
	code = models.CharField("code",max_length=300)
	concept = models.CharField("concept",max_length=300)
	expectedoutput = models.CharField("expectedoutput",max_length=300)
	feedback = models.CharField("feedback",max_length=300)
	feedbackfalse = models.CharField("feedbackfalse",max_length=300)
	help = models.CharField("help",max_length=300)
	input = models.CharField("input",max_length=300)
	inputgenerator = models.CharField("inputgenerator",max_length=300)
	name = models.CharField("name",max_length=300)
	pl_path = models.CharField("pl_path",max_length=300)
	pltest = models.CharField("pltest",max_length=300)
	repository = models.CharField("repository",max_length=300)
	soluce = models.CharField("soluce",max_length=300)
	taboo = models.CharField("taboo",max_length=300)
	tag = models.CharField("tag",max_length=300)
	tagname = models.CharField("tagname",max_length=300)
	testcode = models.CharField("testcode",max_length=300)
	text = models.CharField("text",max_length=300)
	title = models.CharField("title",max_length=300)

class FilesForExercise(models.Model):


gradeData
gradeData:grade
gradeData:grade:error
gradeData:grade:errormessage
gradeData:grade:errormessages
gradeData:grade:execution
gradeData:grade:execution:stderr
gradeData:grade:execution:stdout
gradeData:grade:feedback
gradeData:grade:other
gradeData:grade:plateforme
gradeData:grade:result
gradeData:grade:stderr
gradeData:grade:stdout
gradeData:grade:success
gradeData:platform_error





def addnew(thedata):
	keys = ["author","code","concept","expectedoutput","feedback","feedbackfalse","help","input","inputgenerator","name","pl_path","pltest","repository","soluce","taboo","tag","tagname","testcode","text","title",]



	n = Pldata()
	n.data = thedata
	n.save()


