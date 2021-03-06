from django.conf.urls import include, url
from .views import home, menu, ItemCreateView, ItemDeleteView, ItemListView, ItemDetailView, ItemUpdateView, \
    CategoryListView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView, MenuListView, MenuCreateView, \
    MenuDeleteView, MenuUpdateView,  user_registration, addtoorder, cart, \
    activate_work, activate, permission_denied, removefromorder, checkout, order, ordercomplete, ordersubmit, \
    CommentCreateView, CommentDeleteView, CommentListView, CommentUpdateView, AdminCommentListView, menuview

from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^activates/$', activate, name='activate'),
    url(r'^activate/$', activate_work, name='activate_work'),
    url(r'^ordersubmit$', ordersubmit, name="ordersubmit"),
    url(r'^update_order/(?P<id>\d+)$', ordercomplete, name="completed"),
    url(r'^order$', order, name="order"),
    url(r'^checkout$', checkout, name="checkout"),
    url(r'^removeitem(?P<pk>\d+)$', removefromorder.as_view(), name='remove'),
    url(r'^/permission-denied/', permission_denied, name='denied'),
    url(r'^accounts/login/', login, name="login"),
    url(r'^cart', cart, name="cart"),
    url(r'^logout/', logout, {'next_page': '/'}, name="logout"),
    url(r'^registration/', user_registration, name="user_registration"),
    url(r'^viewmenu(?P<id>\d+)/', menuview, name="viewmenu"),
    url(r'^menu(?P<id>\d+)/', menu, name="menu"),
    url(r'^item_form/', ItemCreateView.as_view(), name="item_form"),
    url(r'^item_list/', ItemListView.as_view(template="item_list.html"), name="item_list"),
    url(r'^delete_item/(?P<pk>\d+)$', ItemDeleteView.as_view(), name="delete_item"),
    url(r'^item_detail/(?P<pk>\d+)$', ItemDetailView.as_view(), name="item_detail"),
    url(r'^item_update/(?P<pk>\d+)$', ItemUpdateView.as_view(), name="item_update"),
    url(r'^category_list/', CategoryListView.as_view(template="category_list.html"), name="category_list"),
    url(r'^category_form/', CategoryCreateView.as_view(), name="category_form"),
    url(r'^delete_category/(?P<pk>\d+)$', CategoryDeleteView.as_view(), name="delete_category"),
    url(r'^update_category/(?P<pk>\d+)$', CategoryUpdateView.as_view(), name="update_category"),
    url(r'^menu_list/', MenuListView.as_view(template="menu_list.html"), name="menu_list"),
    url(r'^menu_form/', MenuCreateView.as_view(), name="menu_form"),
    url(r'^delete_menu/(?P<pk>\d+)$', MenuDeleteView.as_view(), name="delete_menu"),
    url(r'^update_menu/(?P<pk>\d+)$', MenuUpdateView.as_view(), name="update_menu"),
    url(r'^comment_form/', CommentCreateView.as_view(), name="comment_form"),
    url(r'^delete_comment/(?P<pk>\d+)$', CommentDeleteView.as_view(), name="admin_delete_comment"),
    url(r'^comment_list/$', CommentListView.as_view(), name="comment_list"),
    url(r'^admin_comment_list/$', AdminCommentListView.as_view(), name="admin_comment_list"),
    url(r'^comment_update/(?P<pk>\d+)$', CommentUpdateView.as_view(), name="admin_comment_update"),
    url(r'^addtoorder(?P<item_id>\d+)$', addtoorder, name="addtoorder"),
    url(r'^', home, name="home"),
]