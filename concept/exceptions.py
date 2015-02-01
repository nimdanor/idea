__author__ = 'dr'

class CreateCycleException(Exception):
    def __init__(self, c1, c2,mode):
        self.mode = mode
        self.c1 = c1
        self.c2 = c2

    def __str__(self):
        return repr("Creation of a cycle between "+self.c1.name+" and "+self.c2.name+" "+self.mode)