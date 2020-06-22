from app import views
from django.conf.urls import url


app_name = 'score'

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^update/$', views.update, name='update'),
    url(r'^search/$', views.search, name='search'),

]
