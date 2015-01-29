

__author__ = 'dr'


from selenium import webdriver
from django.test import TestCase

class InitialSetUpTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_basic_template_access(self):
        self.browser.get('http://localhost:8000/idea/acceuil.html')
        self.assertIn("Ontologie",self.browser.title)


