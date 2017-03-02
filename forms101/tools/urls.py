from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
#    url(r'^$', views.hello, name='hello'),
    url(r'^$', views.index, name='hello'),

#    url(r'^get_name/$', views.get_name, name='get_name'),
#    url(r'^$', 'views.index', name='index'),
]
