__author__ = 'dr'
from concept.exceptions import CreateCycleException


class MyExceptionMiddleware(object):
    def process_exception(self, request, exception):
        if not isinstance(exception, CreateCycleException):
            return None
        return HttpResponse('<html><body>this would create a cycle in your ontologie go back and change your values </body></html>')
