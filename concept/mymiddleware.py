__author__ = 'dr'

from django.http import HttpResponse
from concept.exceptions import CreateCycleException


class MyExceptionMiddleware(object):
    def process_exception(self, request, exception):

        if not isinstance(exception, CreateCycleException):
            return None
        #stri ="<html><body> {0.c1} is a descendant of {0.c2} </body></html>" % (exception)
        stu = "<H1>this would create a cycle in your ontologie go back and change your values</H1>"
        stri ="<html><body> {m} <p>{e.c1} is a descendant of {e.c2}</p> </body></html>".format(e=exception,m=stu)
        return HttpResponse(stri)
