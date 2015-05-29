from django.conf.urls import  url


from . import views
from polls.views import vote

urlpatterns =  [
        url(r'^$', views.index, name='index'),
        url(r'^(?P<question_id>[0-9])+/$',views.detail,name='detail'),
        url(r'^(?P<question_id>[0-9]+)/results/$',views.detail,name='results'),
        url(r'^(?P<question_id>[0-9]+)/vote/$',views.detail,name='vote'),
]


