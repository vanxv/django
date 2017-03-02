from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[a-z]+)/weather/$', views.weather, name='weather'),
    url(r'^weather/(?P<question_id>[a-z]+)/$', views.weather, name='weather'),
    url(r'^weather/(?P<question_id>[\u4e00-\u9fa5]+)/$', views.weather, name='weather'),

]