

__author__ = 'dr'


from selenium import webdriver
from django.test import TestCase

from concept.models import Concept, Link,getRoots
from concept.exceptions import  CreateCycleException

class InitialSetUpTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def XXXXXtest_insert_and_delete(self):
        '''
        verifier que le lien ne fait pas sauter des dépendances
        si l'on retire un lien il y a deux cas de figure
        1) Full : on retire le lien et tous ces prérequis
        2) local: on retire le lien mais l'on rajoute tous ces dépendatence directes
        Pour tester il faut créer un graphe asser complexe de hauteur 4
        '''
        c1 = Concept(name="racine",lname="plus long la racine : carotte ?",description=" tss tss tss")
        c1.save()
        c2 = Concept(name="variable",lname="px par exemple ?",description=" encore un concept")
        c2.save()
        c3 = Concept(name="Troisième",lname="px mple ?",
                     description=" pfff ")
        c3.save()
        c4 = Concept(name="Quatre",lname="px mple ?",
                     description=" poliveau ")
        c4.save()
        c5 = Concept(name="CINQ",lname="px mple ?",
                     description="  entre la rue de Vanve et la rue didot")
        c5.save()

        l1= Link(ascendant=c1,descendant=c2)
        l1.save()
        l1= Link(ascendant=c1,descendant=c5)
        l1.save()
        l1= Link(ascendant=c1,descendant=c4)
        l1.save()
        l2= Link(ascendant=c2,descendant=c3)
        l2.save()
        l3 =Link(ascendant=c3,descendant=c4)
        l3.save()
        l4 =Link(ascendant=c4,descendant=c5)
        l4.save()
        self.assertEqual(6,Link.objects.all().count())
        self.browser.get('http://localhost:8000/concept/graph/1/')

    def XXXXtest_basic_template_access(self):
        self.browser.get('http://localhost:8000/idea/acceuil.html')
        self.assertIn("Ontologie",self.browser.title)
        self.assertIn("<html",self.browser.page_source)
        self.assertIn("Revuz",self.browser.page_source)
        try:
            self.browser.find_element_by_id("content")
            self.browser.find_element_by_id("nav")
        except:
            self.fail("no id='nav' div in page")

        if 'GROSTEXTDELAMORTQUITUE' in self.browser.page_source:
            self.fail("encore un problème avec le type de la variable image ")



class TestOfConceptAndLink(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_direct_cycle(self):
        c1 = Concept(name="racine",lname="plus long la racine : carotte ?",description=" tss tss tss")
        c1.save()
         # remarque cette méthode count évite de créer le quéry set et utilise le sql directement
        self.assertEqual(Concept.objects.all().count(),1)
        c2 = Concept(name="variable",lname="px par exemple ?",description=" encore un concept")
        c2.save()
        self.assertEqual(Concept.objects.all().count(),2)
        l1=Link(descendant=c2,ascendant=c1)
        l1.save()
        print(l1)
        self.assertEqual(Link.objects.all().count(),1)
        l2=Link(descendant=c1,ascendant=c2)
        try:
            l2.save() # ceci doit échouer car cela créerai un cycle
        except CreateCycleException as e:
            print(e)
        except Exception :
            self.fail("din't raise CreateCycleException")
        self.assertEqual(Link.objects.all().count(),1)


    def test_indirect_cycle(self):
        c1 = Concept(name="racine",lname="plus long la racine : carotte ?",description=" tss tss tss")
        c1.save()
        c2 = Concept(name="variable",lname="px par exemple ?",description=" encore un concept")
        c2.save()
        c3 = Concept(name="Troisième",lname="px mple ?",
                     description=" encore un concept pour une detection lointaine de cycle")
        c3.save()

        l1= Link(ascendant=c1,descendant=c2)
        l2= Link(ascendant=c2,descendant=c3)
        l3 =Link(ascendant=c3,descendant=c1)
        l1.save()
        l2.save()
        try:
            l3.save() # ceci doit échouer car cela créerai un cycle indirect
        except CreateCycleException as e:
            print(e)
        except Exception :
            self.fail("din't raise CreateCycleException")

        self.assertEqual(Link.objects.all().count(),2) # y en a 3



    def test_root(self):
        c1=Concept(name="racine",lname="plus long la racine : carotte ?",description=" tss tss tss")
        c1.save()
        self.assertEqual([c1],getRoots())
        self.fail("tss tss")

    def test_insert_and_delete(self):
        '''
        verifier que le lien ne fait pas sauter des dépendances
        si l'on retire un lien il y a deux cas de figure
        1) Full : on retire le lien et tous ces prérequis
        2) local: on retire le lien mais l'on rajoute tous ces dépendatence directes
        Pour tester il faut créer un graphe asser complexe de hauteur 4
        '''
        c1 = Concept(name="racine",lname="plus long la racine : carotte ?",description=" tss tss tss")
        c1.save()
        c2 = Concept(name="variable",lname="px par exemple ?",description=" encore un concept")
        c2.save()
        c3 = Concept(name="Troisième",lname="px mple ?",
                     description=" pfff ")
        c3.save()
        c4 = Concept(name="Quatre",lname="px mple ?",
                     description=" poliveau ")
        c4.save()
        c5 = Concept(name="CINQ",lname="px mple ?",
                     description="  entre la rue de Vanve et la rue didot")
        c5.save()

        l1= Link(ascendant=c1,descendant=c2)
        l1.save()
        l1= Link(ascendant=c1,descendant=c5)
        l1.save()
        l1= Link(ascendant=c1,descendant=c4)
        l1.save()
        l2= Link(ascendant=c2,descendant=c3)
        l2.save()
        l3 =Link(ascendant=c3,descendant=c4)
        l3.save()
        l4 =Link(ascendant=c4,descendant=c5)
        l4.save()
        self.assertEqual(6,Link.objects.all().count())