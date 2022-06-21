from django.conf.urls import url

urlpatterns = patterns('ask.qa',
    url(r'^$', 'test', name = 'root'),
    url(r'^login/$', 'test', name = 'login'),
    url(r'^signup/$', 'test', name = 'signup'),
    url(r'^question/(?P<ID>d+)$', 'test', name = 'question'),
    url(r'^ask/$', 'test', name = 'ask'),
    url(r'^popular/$', 'test', name = 'popular'),
    url(r'^new/$', 'test', name = 'new'),
)