from django.conf.urls import include, url
from .views import home, ItemCreateView, ItemDeleteView, ItemListView


urlpatterns = [

    url(r'^item_form/', ItemCreateView.as_view(), name="item_form"),
    url(r'^item_list/', ItemListView.as_view(template="item_list.html"), name="item_list"),
    url(r'^delete_item/(?P<pk>\d+)$', ItemDeleteView.as_view(), name="delete_item"),
    url(r'^', home, name="home"),



]