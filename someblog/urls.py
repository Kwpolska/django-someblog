from django.conf.urls import url

from someblog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>.+)/$', views.post, name='post'),
    url(r'^tag/(?P<slug>.+)/$', views.tag, name='tag'),
]
