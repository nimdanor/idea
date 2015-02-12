


1) Installer pip3 et virtualenv 

sudo apt-get install python3-pip 
sudo pip3 install virtualenv

2)creer un environement 

	cd ~
	virtualenv -p /usr/bin/python3 DJANGO 

3) Installer Django dans cet  environement 

	source ~/DJANGO/bin/activate 
	pip3 install django

4) Tada 

	vous pouver tester en local le projet 
	cd concepts
	python3 manage runserver
	firefox http://127.0.0.1:8000/
5) Deployement
	definir la variable environnement
	SECRET_KEY = '^-k1d$y2mv_x+n06eyf-!l9&#n0&)5-hhv)h*r=(!c6l8!ad++'


