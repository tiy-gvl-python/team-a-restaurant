from django.conf.urls import include, url
from restaurant_app.views import home, menuactchoice, menu, ItemCreateView, ItemDeleteView, ItemListView, ItemDetailView, ItemUpdateView, CategoryListView, \
    CategoryCreateView, CategoryDeleteView, CategoryUpdateView

urlpatterns = [

    url(r'^menuactlist', menuactchoice, name="menuactlist"),
    url(r'^me/(?P<id>\d+)nu/', menu, name="menu"),
    url(r'^item_form/', ItemCreateView.as_view(), name="item_form"),
    url(r'^item_list/', ItemListView.as_view(template="item_list.html"), name="item_list"),
    url(r'^delete_item/(?P<pk>\d+)$', ItemDeleteView.as_view(), name="delete_item"),
    url(r'^item_detail/(?P<pk>\d+)$', ItemDetailView.as_view(), name="item_detail"),
    url(r'^item_update/(?P<pk>\d+)$', ItemUpdateView.as_view(), name="item_update"),
    url(r'^category_list/', CategoryListView.as_view(template="category_list.html"), name="category_list"),
    url(r'^category_form/', CategoryCreateView.as_view(), name="category_form"),
    url(r'^delete_category/(?P<pk>\d+)$', CategoryDeleteView.as_view(), name="delete_category"),
    url(r'^update_category/(?P<pk>\d+)$', CategoryUpdateView.as_view(), name="update_category"),
    url(r'^', home, name="home"),
]