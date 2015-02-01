__author__ = 'dr'
from django.conf.urls import patterns, include, url
from concept import views



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'idea.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.racine),
    # vue par default des concepts
    url(r'^(?P<concept_id>\d+)/$', views.default),
    # vue simplifiée
    # url(r'^simple/(?P<concept_id>?\d+)/$', views.simple),
    #url(r'^graph$', views.graph),
)
