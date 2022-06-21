from qa.urls import test
from django.urls import include, path

urlpatterns = patterns('qa.views',
    url(r'^$', test, name = 'root'),
    url('login/', test, name = 'login'),
    url('signup/', test, name = 'signup'),
    url(r'^question/(?P<ID>\d+)$', test, name = 'question'),
    url('ask/', test, name = 'ask'),
    url('popular/', test, name = 'popular'),
    url('new/', test, name = 'new'),
)