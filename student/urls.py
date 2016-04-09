
__author__ = 'dr'
from django.conf.urls import patterns, include, url
from student import views



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'idea.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # vue par default des concepts le graph
	url(r'^$', views.students),
	url(r'^stuaddconcept/(?P<studid>\d+)/$',views.chooseconcept),
	url(r'^stuaddconcept/(?P<student_id>\d+)/(?P<concept_id>\d+)/(?P<level>\d+)$', views.stuaddconcept),

)

