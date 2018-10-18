from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/edit2/$', views.post_edit2, name='post_edit2'),
    url(r'^post/(?P<pk>\d+)/edit3/$', views.post_edit3, name='post_edit3'),
    #url(r'^list/$', views.listing, name='listing'),


]
