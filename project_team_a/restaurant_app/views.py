from django.shortcuts import render, render_to_response

# Create your views here.
from restaurant_app.models import Menu, Category, Item


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