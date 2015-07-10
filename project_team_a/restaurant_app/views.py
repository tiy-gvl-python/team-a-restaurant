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


def menu(requests, id, cid):
    context = {}
    if int(cid):
        catedisplay = Category.objects.get(id=cid)
        catedisplay = catedisplay.items.all()
        print(catedisplay)
        context["catedisplay"] = catedisplay
    menu = Menu.objects.get(id=id, display=True)
    cate = menu.categories.all()
    print(menu)
    context['catmenu'] = menu
    context["cate"] = cate
    context["id"] = id
    print(context)
    return render_to_response("usermenu.html", context)