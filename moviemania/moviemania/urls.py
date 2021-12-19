from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^find', views.find, name='find'),
    url(r'^add', views.add, name='add'),
    url(r'^watchlist', views.watchlist, name = 'watchlist')
]

app_name = 'movie'
