from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'idea.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^idea/(?P<name>[^.]+).html$',  views.acceuil),
    url(r'^concept/',include('concept.urls')),
    url(r'^$',  views.index),


)
