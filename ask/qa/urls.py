from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'ask.qa.test', name = 'root'),
    url(r'^login/$', 'ask.qa.test', name = 'login'),
    url(r'^signup/$', 'ask.qa.test', name = 'signup'),
    url(r'^question/(?P<ID>d+)$', 'ask.qa.test', name = 'question'),
    url(r'^ask/$', 'ask.qa.test', name = 'ask'),
    url(r'^popular/$', 'ask.qa.test', name = 'popular'),
    url(r'^new/$', 'ask.qa.test', name = 'new'),
]