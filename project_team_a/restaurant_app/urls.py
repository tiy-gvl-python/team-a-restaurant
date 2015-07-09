from django.conf.urls import include, url
from restaurant_app.views import home

urlpatterns = [

    url(r'^', home, name="home"),


]