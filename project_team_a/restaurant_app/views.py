from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Item, Category, Menu, Profile, Comments
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.template import RequestContext
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .custom_wrappers import staff_wrapper_func, customer_wrapper_func, owner_wrapper_func





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

class UserRegistration(FormView):
    #model = Profile
    pass

# comments section
class CommentCreateView(CreateView):
    model = Comments
    fields = ['user', 'comment', 'recommend']
    success_url = reverse_lazy('restaurant_app:comments_form')

class CommentDeleteView(DeleteView):
    model = Comments
    success_url = reverse_lazy('restaurant_app:comments_list')

class CommentUpdateView(UpdateView):
    model = Comments
    success_url = reverse_lazy('restaurant_app:comments_list')

class CommentsListView(ListView):
    model = Comments
    success_url = reverse_lazy('restaurant_app:comments_list')
    template="comments_list.html"

# end comments section

def user_profile_registration(request):
    if request.POST:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        customer = request.POST.get('customer')
        staff = request.POST.get('staff')
        owner = request.POST.get('owner')


        user_form = UserProfileForm({
            'username': username,
            'password1': password1,
            'password2': password2,
            'phone': phone,
            'customer': customer,
            'staff': staff,
            'owner': owner,


        })
        try:
            user_form.save(commit=True)
            return HttpResponseRedirect("/")
        except ValueError:
            return render_to_response("registration/create_user.html",
                                      {'form': user_form},
                                      context_instance=RequestContext(request))

    return render_to_response("registration/create_user.html",
                              {'form': UserProfileForm()},
                              context_instance=RequestContext(request))
