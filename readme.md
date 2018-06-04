


1) Installer pip3 et virtualenv 

sudo apt-get install python3-pip 
sudo pip3 install virtualenv

2)creer un environement 

	cd ~
	virtualenv -p /usr/bin/python3 DJANGO 

3) Installer Django dans cet  environement 

	source ~/DJANGO/bin/activate  
	pip3 install django  
	pip3 install django-jsonview  

4) Tada 

	vous pouver tester en local le projet   
	cd concepts  
	python3 manage makemigrations  
	python3 manage runserver  
	firefox http://127.0.0.1:8000/  
5) Deployement
	definir la variable environnement
	SECRET_KEY = 'votre clef genere avec une commande adaptee'

	definir les url pl.univ-mlv.fr (premier langage)
 	DEBUG=False 
	dans le fichier settings.py 
	definir la base de donnée  
	python3 manage.py makemigrations  
	python3 manage.py migrate  
	python3 manage.py createsuperuser  
6) lancer le server 
	python3 manage.py runserver  
	ou sont les logs ?

