from django.conf.urls import include, url
from restaurant_app.views import home, menu

urlpatterns = [

    url('r^menu', menu, name="menu")
    url(r'^', home, name="home"),


]