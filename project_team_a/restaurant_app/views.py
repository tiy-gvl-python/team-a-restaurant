from django.shortcuts import render, render_to_response
from restaurant_app.models import Menu, Category, Item
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Item, Category,

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
    fields = ['name']
    success_url = reverse_lazy('restaurant_app:category_form')

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('restaurant_app:category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    template = "update_category.html"
    success_url = reverse_lazy('restaurant_app:category_list')
