from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Item, Category, Menu, Order, Profile
from django.http import HttpResponseNotFound, HttpResponseRedirect

def home(requests):
    return render_to_response("home.html")


def menuactchoice(requests):
    menu_act = Menu.objects.filter(display=True)
    print(menu_act)
    context = {"menus": menu_act}
    return render_to_response("menuchoice.html", context)


def menu(requests, id):
    context = {}
    categories = []
    category_items = []
    items = []
    menu = Menu.objects.get(id=id, display=True)
    cate = menu.categories.all()
    for ca in cate:
        if items:
            print("Items", items)
            category_items.append(items)
            items = []
        categories.append(ca)
        for item in ca.items.all():
            print("Item", item)
            items.append(item)
            print("Items list", items)
    if items:
        print("Items", items)
        category_items.append(items)
    print("Category", categories,"Category Items", category_items)
    print(menu)
    context['catmenu'] = menu
    context["cate"] = categories
    context["id"] = id
    context["citems"] = category_items
    context["index"] = range(len(cate))
    print("Dictionary", context)
    return render_to_response("menuchoice.html", context)

def cart(request, user_id):
    context = {}
    if not Order.objects.filter(user = Profile.objects.filter(user_id=user_id)):
        profile = Profile.objects.get(user_id = user_id)
        order = Order.objects.create(user = Profile.objects.get(user_id=user_id), submit=False, completed=False )
        order.save()
        print("RAN")
        context = {'order': order.items}
        # Made new Order
    elif Order.objects.filter(user = Profile.objects.filter(user_id=user_id), submit=True, completed=True):
        order = Order.objects.create(user = Profile.objects.filter(user_id=user_id), submit=False, completed=False )
        order.save()

    elif Order.objects.filter(user = Profile.objects.filter(user_id=user_id), submit = True):
        # Needs to go to a being proccessed page
        pass

    else:
        order = Order.objects.filter(user = Profile.objects.filter(user_id = user_id), submit=False, completed = False)
        print(order)
        context = {'order': list(order)[0].items.all()}
    print(order)
    return render_to_response("cart.html", context)




class ItemListView(ListView):
    model = Item
    template = "item_list.html"


class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'price', 'description']
    success_url = reverse_lazy('restaurant_app:item_form')


class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('restaurant_app:item_list')

class ItemDetailView(DetailView):
    model = Item
    success_url = reverse_lazy('restaurant_app:item_form')

class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name', 'price', 'description']
    template = "item_update"
    success_url = reverse_lazy('restaurant_app:item_list')

class CategoryListView(ListView):
    model = Category
    template = "category_list.html"

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'items']
    success_url = reverse_lazy('restaurant_app:category_form')

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('restaurant_app:category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'items']
    template = "update_category.html"
    success_url = reverse_lazy('restaurant_app:category_list')

class MenuListView(ListView):
    model = Menu
    template = "menu_list.html"

class MenuCreateView(CreateView):
    model = Menu
    fields = ['categories', 'display', 'name']
    success_url = reverse_lazy('restaurant_app:menu_form')

class MenuDeleteView(DeleteView):
    model = Menu
    success_url = reverse_lazy('restaurant_app:menu_list')

class MenuUpdateView(UpdateView):
    model = Menu
    fields = ['categories', 'display', 'name']
    template = "update_menu.html"
    success_url = reverse_lazy('restaurant_app:menu_list')









