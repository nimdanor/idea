__author__ = 'dr'
from django.conf.urls import patterns, include, url
from concept import views



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'idea.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # vue par default des concepts le graph
    url(r'^$', views.listing),
    url(r'^listing/$', views.listing),
    url(r'^level/$', views.level),
	url(r'^debug/(?P<concept_id>\d+)/$', views.debugview),
    url(r'^create/$', views.create),
    url(r'^graph/$', views.graphRL),
    url(r'^graph/RL/$', views.graphRL),
    url(r'^graph/TB/$', views.graphTB),
    url(r'^graph/BT/$', views.graphBT),
    url(r'^graph/LR/$', views.graphLR),
    url(r'^addlink/(?P<concept_id>\d+)/$', views.addPreLink),
    url(r'^edit/(?P<concept_id>\d+)/$', views.edit),
    url(r'^graph/(?P<concept_id>\d+)/$', views.graphTT),
    url(r'^export/(?P<type>\w+)/$',views.export),
    url(r'^k/(?P<concept_id>\d+)/$', views.knowls),
    url(r'^json/$', views.jsonview),
    url(r'^only/$', views.onlyGraph),

    #url(r'^edit/(?P<concept_id>\d+)/$', views.edit),
    # vue simplifiée
    # url(r'^simple/(?P<concept_id>?\d+)/$', views.simple),


)
