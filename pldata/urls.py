
__author__ = 'dr'
from django.conf.urls import patterns, include, url
from pldata import views



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'idea.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # vue par default des concepts le graph
	url(r'^add$', views.addnewdata),
	url(r'^view$',views.viewsdata)

)

