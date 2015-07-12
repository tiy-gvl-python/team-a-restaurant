from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Item, Category, Menu, Profile, Order
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.template import RequestContext
from .forms import ProfileForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from .custom_wrappers import staff_wrapper_func, customer_wrapper_func, owner_wrapper_func

def addtoorder(requests, user_id, item_id):
    user_id = requests.user
    order = Order.objects.get(user = Profile.objects.get(user=user_id))
    order.items.add(Item.objects.get(id = item_id))
    order.save()

def cart(requests):
    context = {}
    user_id = requests.user
    if Order.objects.filter(user=Profile.objects.get(user=user_id), submit=False, completed=False):
        order = Order.objects.filter(user=Profile.objects.get(user=user_id), submit=False, completed=False)
        context['items'] = order.items.all()
    elif bool(Order.objects.filter(user=Profile.objects.get(user=user_id), submit=True, completed=True)):
        order = Order.objects.create(user=Profile.objects.get(user=user_id), submit=False, completed=True)
        order.save()
        context['status'] = "Cart is empty"
    elif bool(Order.objects.filter(user=Profile.objects.get(user=user_id))):
        order = Order.objects.create(user=Profile.objects.get(user=user_id), submit=False, completed=True)
        order.save()
        context['status'] = "Cart is empty"
    else:
        context['status'] = "Order is being proccessed: Call Here"
    return render_to_response("cart.html", context, context_instance=RequestContext(requests))


def home(requests):
    return render_to_response("home.html", context_instance=RequestContext(requests))

def menu(requests, id):
    context = {}
    menu_act = Menu.objects.filter(display=True)
    print(int(id))
    if int(id):
        print("RUNNING")
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
    else:
        context['index'] = -1
    context["menus"] = menu_act
    return render_to_response("menuchoice.html",
                              context,
                              context_instance=RequestContext(requests))


class ItemListView(ListView):
    model = Item
    template = "item_list.html"


class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'price', 'description']
    success_url = reverse_lazy('restaurant_app:item_form')

    @method_decorator(user_passes_test(owner_wrapper_func,
                                       redirect_field_name='restaurant_app:denied',
                                       login_url='restaurant_app:denied',
                                       ))
    def dispatch(self, *args, **kwargs):
        print("user passed test", owner_wrapper_func)
        return super().dispatch(*args, **kwargs)


class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('restaurant_app:item_list')

    @method_decorator(user_passes_test(owner_wrapper_func,
                                       redirect_field_name='restaurant_app:denied',
                                       login_url='restaurant_app:denied',
                                       ))
    def dispatch(self, *args, **kwargs):
        print("user passed test", owner_wrapper_func)
        return super().dispatch(*args, **kwargs)


class ItemDetailView(DetailView):
    model = Item
    success_url = reverse_lazy('restaurant_app:item_form')

    @method_decorator(login_required(redirect_field_name='restaurant_app:login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name', 'price', 'description']
    template = "item_update"
    success_url = reverse_lazy('restaurant_app:item_list')

    @method_decorator(user_passes_test(owner_wrapper_func,
                                       redirect_field_name='restaurant_app:denied',
                                       login_url='restaurant_app:denied',
                                       ))
    def dispatch(self, *args, **kwargs):
        print("user passed test", owner_wrapper_func)
        return super().dispatch(*args, **kwargs)

class CategoryListView(ListView):
    model = Category
    template = "category_list.html"


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'items']
    success_url = reverse_lazy('restaurant_app:category_form')

    @method_decorator(user_passes_test(owner_wrapper_func,
                                       redirect_field_name='restaurant_app:denied',
                                       login_url='restaurant_app:denied',
                                       ))
    def dispatch(self, *args, **kwargs):
        print("user passed test", owner_wrapper_func)
        return super().dispatch(*args, **kwargs)


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('restaurant_app:category_list')

    @method_decorator(user_passes_test(owner_wrapper_func,
                                       redirect_field_name='restaurant_app:denied',
                                       login_url='restaurant_app:denied',
                                       ))
    def dispatch(self, *args, **kwargs):
        print("user passed test", owner_wrapper_func)
        return super().dispatch(*args, **kwargs)


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'items']
    template = "update_category.html"
    success_url = reverse_lazy('restaurant_app:category_list')

    @method_decorator(user_passes_test(owner_wrapper_func,
                                       redirect_field_name='restaurant_app:denied',
                                       login_url='restaurant_app:denied',
                                       ))
    def dispatch(self, *args, **kwargs):
        print("user passed test", owner_wrapper_func)
        return super().dispatch(*args, **kwargs)

class MenuListView(ListView):
    model = Menu
    template = "menu_list.html"

class MenuCreateView(CreateView):
    model = Menu
    fields = ['categories', 'display', 'name']
    success_url = reverse_lazy('restaurant_app:menu_form')

    @method_decorator(user_passes_test(owner_wrapper_func,
                                       redirect_field_name='restaurant_app:denied',
                                       login_url='restaurant_app:denied',
                                       ))
    def dispatch(self, *args, **kwargs):
        print("user passed test", owner_wrapper_func)
        return super().dispatch(*args, **kwargs)


class MenuDeleteView(DeleteView):
    model = Menu
    success_url = reverse_lazy('restaurant_app:menu_list')

    @method_decorator(user_passes_test(owner_wrapper_func,
                                       redirect_field_name='restaurant_app:denied',
                                       login_url='restaurant_app:denied',
                                       ))
    def dispatch(self, *args, **kwargs):
        print("user passed test", owner_wrapper_func)
        return super().dispatch(*args, **kwargs)


class MenuUpdateView(UpdateView):
    model = Menu
    fields = ['categories', 'display', 'name']
    template = "update_menu.html"
    success_url = reverse_lazy('restaurant_app:menu_list')

    @method_decorator(user_passes_test(owner_wrapper_func,
                                       redirect_field_name='restaurant_app:denied',
                                       login_url='restaurant_app:denied',
                                       ))
    def dispatch(self, *args, **kwargs):
        print("user passed test", owner_wrapper_func)
        return super().dispatch(*args, **kwargs)


# Pj helped me get out of a whole
def user_registration(request):
    if request.POST:
        ok = True
        user_creation_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if not user_creation_form.is_valid():
            ok = False
        if not profile_form.is_valid():
            ok = False
        if ok:
            try:
               user = user_creation_form.save()
               profile = profile_form.save(commit=False)
               profile.user = user
               profile.save()
               return redirect('home')
            except:
                return render_to_response("registration/create_user.html",
                                      {'u_form': UserCreationForm, 'p_form': ProfileForm},
                                      context_instance=RequestContext(request))
    return render_to_response("registration/create_user.html",
                                  {'u_form': UserCreationForm(), 'p_form': ProfileForm()},
                                  context_instance=RequestContext(request))


def permission_denied(requests):
    return render_to_response("restaurant_app/permission_denied.html",
                              context_instance=RequestContext(requests))