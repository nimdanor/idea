

__author__ = 'dr'


from selenium import webdriver
from django.test import TestCase

from concept.models import Concept, Link,getRoots
from concept.exceptions import  CreateCycleException



class TestConceptAndLinkWithOutBrowser(TestCase):
    def setUp(self):
        c1 = Concept(name="racine",lname="plus long la racine : carotte ?",description=" tss tss tss")
        c1.save()
        c1.delete()
        self.assertEqual(c1.pk,1)


    def tearDown(self):
        pass


    def testDelete(self):
        self.assertEqual(1,Concept.objects.count())
        ck = Concept(name="Bob",lname="un nom plus long ",description=" tss tss tss")
        ck.save()
        ck.delete()
        self.assertEqual(1,len(Concept.objects.all()))


    def test_direct_cycle(self):

         # remarque cette méthode count évite de créer le quéry set et utilise le sql directement
        self.assertEqual(Concept.objects.all().count(),1)
        c2 = Concept(name="variable",lname="px par exemple ?",description=" encore un concept")
        c2.save()


        self.assertEqual(Concept.objects.all().count(),2)
        c1=Concept.racine()
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
        #c1 = Concept(name="racine",lname="plus long la racine : carotte ?",description=" tss tss tss")
        #c1.save()
        c2 = Concept(name="variable",lname="px par exemple ?",description=" encore un concept")
        c2.save()
        c3 = Concept(name="Troisième",lname="px mple ?",
                     description=" encore un concept pour une detection lointaine de cycle")
        c3.save()

        l1= Link(ascendant=Concept.racine(),descendant=c2)
        l2= Link(ascendant=c2,descendant=c3)
        l3 =Link(ascendant=c3,descendant=Concept.racine())
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
        '''
        verifie le fonctionnement de la méthode getRoots
        :return:
        '''
        x=[]
        for cc in Concept.objects.all():
            x.append(cc)
        self.assertEqual(x,getRoots())

    def test_insert_and_delete(self):
        '''
        verifier que le lien ne fait pas sauter des dépendances
        si l'on retire un lien il y a deux cas de figure
        1) Full : on retire le lien et tous ces prérequis
        2) local: on retire le lien mais l'on rajoute tous ces dépendatence directes
        Pour tester il fau1t créer un graphe asser complexe de hauteur 4
        '''
        c1 = Concept.racine()
        c2 = Concept(name="variable",lname="px par exemple ?",description=" encore un concept")
        c2.save()
        self.assertEqual(1,Link.objects.all().count()) # création automatique du lien vers la racine
        c3 = Concept(name="Troisième",lname="px mple ?",
                     description=" pfff ")
        c3.save()
        c4 = Concept(name="Quatre",lname="px mple ?",
                     description=" poliveau ")
        c4.save()
        c5 = Concept(name="CINQ",lname="px mple ?",
                     description="  entre la rue de Vanve et la rue didot")
        c5.save()
        #  creation des  liens avec la racine automatique donc 4 liens après la création de 5 concepts
        self.assertEqual(4,Link.objects.all().count())
        l2= Link(ascendant=c2,descendant=c3)
        l2.save()
        # le lien c3 -> c1 disparait
        self.assertEqual(4,Link.objects.all().count())
        l3 =Link(ascendant=c3,descendant=c4)
        l3.save()
        # le lien c4 -> c1 est retiré
        self.assertEqual(4,Link.objects.all().count())
        l4 =Link(ascendant=c4,descendant=c5)
        l4.save()
        # idem
        self.assertEqual(4,Link.objects.all().count())
        Concept.objects.filter(pk=1).delete()
        # ne pas effacer la racine
        self.assertEqual(4,Link.objects.all().count())



class WebInterfaceTest(TestCase):
    #   base = 'http://localhost:8000/' # pour les tests en ligne substituer par le nom du site
    def setUp(self):
        self.base = 'http://localhost:8000/' # pour les tests en ligne substituer par le nom du site
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()


    def pageTest(self,url):
        print(url)
        url = self.base+url
        print(url)
        return
        self.browser.get(url)
        self.assertIn("<html",self.browser.page_source) # page existante pas de bug
        self.assertIn("Revuz",self.browser.page_source) # affiche le copyright en bas
        self.assertIn("bugzilla",self.browser.page_source) # affiche le lien sur bugzilla

    def Xtest_basic_web_access(self):
        self.pageTest('')
        self.pageTest('idea/acceuil.html')  # racine du site
        if 'GROSTEXTDELAMORTQUITUE' in self.browser.page_source:
            self.fail("encore un problème avec le type de la variable image ")

    def testlevelinconcept(self):
        self.pageTest('concept/level/')