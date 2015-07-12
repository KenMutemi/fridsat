from django.conf.urls import patterns, url
from front import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='home'),
    url(r'^publish/$', views.publish, name='publish'),
    url(r'^category/$', views.category, name='category'),
)
