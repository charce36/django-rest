from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.SnippetDetail),
]

urlpatterns = format_suffix_patterns(urlpatterns)