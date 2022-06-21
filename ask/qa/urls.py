from qa.urls import test
from django.urls import include, path

urlpatterns = patterns('qa.views',
    path('', test, name = 'root'),
    path('login/', test, name = 'login'),
    path('signup/', test, name = 'signup'),
    path('question/<int:ID>', test, name = 'question'),
    path('ask/', test, name = 'ask'),
    path('popular/', test, name = 'popular'),
    path('new/', test, name = 'new'),
)