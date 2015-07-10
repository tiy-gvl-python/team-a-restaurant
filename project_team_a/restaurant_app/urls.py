from django.conf.urls import include, url
from restaurant_app.views import home, menuactchoice, menu

urlpatterns = [

    url(r'^menuactlist', menuactchoice, name="menuactlist"),
    url(r'^me/(?P<id>\d+)nu/', menu, name="menu"),
    url(r'^', home, name="home"),


]