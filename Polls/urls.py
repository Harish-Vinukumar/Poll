from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'Polls'


urlpatterns = [

    path('polls/', views.pollsIndex, name='pollsIndex'),
    url(r'^polls/(?P<question_id>[0-9]+)/$', views.details, name='details'),
    url(r'^polls/(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^polls/(?P<question_id>[0-9]+)/votes/$', views.votes, name='votes'),
]
