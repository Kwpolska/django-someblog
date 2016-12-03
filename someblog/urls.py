from django.conf.urls import url

from someblog import views

urlpatterns = [
    url(r'^$', views.index, name='someblog.index'),
    url(r'^post/(?P<slug>.+)/$', views.post, name='someblog.post'),
    url(r'^tags/$', views.tags, name='someblog.tags'),
    url(r'^tag/(?P<slug>.+)/$', views.tag, name='someblog.tag'),
    url(r'^authors/$', views.authors, name='someblog.authors'),
    url(r'^author/(?P<slug>.+)/$', views.author, name='someblog.author'),
]
