from django.conf.urls import include, url
from .views import home, ItemCreateView, ItemDeleteView, ItemListView, ItemDetailView, ItemUpdateView


urlpatterns = [

    url(r'^item_form/', ItemCreateView.as_view(), name="item_form"),
    url(r'^item_list/', ItemListView.as_view(template="item_list.html"), name="item_list"),
    url(r'^delete_item/(?P<pk>\d+)$', ItemDeleteView.as_view(), name="delete_item"),
    url(r'^item_detail/(?P<pk>\d+)$', ItemDetailView.as_view(), name="item_detail"),
    url(r'^item_update/(?P<pk>\d+)$', ItemUpdateView.as_view(), name="item_update"),
    url(r'^', home, name="home"),



]