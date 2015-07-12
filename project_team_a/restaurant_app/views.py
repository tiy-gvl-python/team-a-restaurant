from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Item, Category, Menu, Profile, Order, Count
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.template import RequestContext
from .forms import ProfileForm, ProfileEditForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from .custom_wrappers import staff_wrapper_func, customer_wrapper_func, owner_wrapper_func


# login required for everything but home page permission denied menu and registration

@login_required
def addtoorder(requests, item_id):
    if requests.POST:
        user_id = requests.user.id
        user_id = User.objects.get(id=user_id)
        print("Made it to here")
        order = Order.objects.get(user = Profile.objects.get(user=user_id), submit=False)
        print(order)
        itemcount = Count.objects.create(item=Item.objects.get(id = item_id), order = order, count = requests.POST['count'])
        order.save()
        itemcount.save()
        menu_id = int(requests.POST['menu'])
        print(menu_id)
        return redirect('restaurant_app:menu', id=menu_id)


@user_passes_test(staff_wrapper_func,
                  redirect_field_name='restaurant_app:denied',
                  login_url='restaurant_app:denied')
def order(requests):
    # staff
    context = {}
    ocounts = []
    orders = Order.objects.filter(submit=True, completed=False)
    for order in orders:
        counts = Count.objects.filter(order=order)
        print(counts[0].item)
        ocounts.append((order, counts))
    context['ocounts'] = ocounts
    return render_to_response("staff.html", context, context_instance=RequestContext(requests))


@user_passes_test(staff_wrapper_func,
                  redirect_field_name='restaurant_app:denied',
                  login_url='restaurant_app:denied')
def ordercomplete(requests, id):
    order_object = Order.objects.get(id = int(id))
    order_object.completed = True
    order_object.save()
    # staff
    return redirect('restaurant_app:order')

@login_required
def ordersubmit(requests):
    order = requests.POST['order']
    order_object = Order.objects.get(id = int(order))
    order_object.submit = True
    order_object.save()
    context={'order':int(order)}
    return render_to_response("proccess.html",context, context_instance=RequestContext(requests))

@login_required
def checkout(requests):
    context = {}
    itemtuple = []
    order = requests.POST['order']
    print(order)
    context['order'] = order
    #order = Order.objects.get(id=orderid)
    counts = Count.objects.filter(order=order)
    context['counts'] = counts
    total = 0
    print("Here")
    for count in counts:
        print(count.item.name, count.item.price , count.count)
        itemtuple.append((count.item.name, count.item.price * count.count))
        total +=  count.item.price * count.count
    context["total"] = total
    context["items"] = itemtuple
    return render_to_response("checkout.html", context, context_instance=RequestContext(requests))


class removefromorder(DeleteView):
    model = Count
    success_url = reverse_lazy('restaurant_app:cart')

    @method_decorator(login_required(redirect_field_name='restaurant_app:login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@login_required
def cart(requests):
    context = {}
    user_id = requests.user.id
    user_id = User.objects.get(id=user_id)
    #print("Check if no cart", bool(Order.objects.filter(user=Profile.objects.get(user=user_id))))
    #print("Check if needs new cart", bool(Order.objects.filter(user=Profile.objects.get(user=user_id), submit=True, completed=True)))
    #print("Check if Cart is set", bool(Order.objects.filter(user=Profile.objects.get(user=user_id), submit=False, completed=False)))
    if Order.objects.filter(user=Profile.objects.get(user=user_id), submit=False, completed=False):
        order = Order.objects.get(user=Profile.objects.get(user=user_id), submit=False, completed=False)
        items = Count.objects.filter(order=order)
        print("Here")
        print(bool(len(items)))
        if bool(len(items)):
            print("Made it")
            context['items'] = items
            context['order'] = order.id
            #context['orderobject'] = order
    elif bool(Order.objects.filter(user=Profile.objects.get(user=user_id), submit=True, completed=True)):
        order = Order.objects.create(user=Profile.objects.get(user=user_id), submit=False, completed=False)
        order.save()
        context['status'] = "Cart is empty"
    elif not bool(Order.objects.filter(user=Profile.objects.get(user=user_id))):
        order = Order.objects.create(user=Profile.objects.get(user=user_id), submit=False, completed=False)
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

    @method_decorator(user_passes_test(owner_wrapper_func,
                                       redirect_field_name='restaurant_app:denied',
                                       login_url='restaurant_app:denied',
                                       ))
    def dispatch(self, *args, **kwargs):
        print("user passed test", owner_wrapper_func)
        return super().dispatch(*args, **kwargs)

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

    @method_decorator(user_passes_test(owner_wrapper_func,
                                       redirect_field_name='restaurant_app:denied',
                                       login_url='restaurant_app:denied',
                                       ))
    def dispatch(self, *args, **kwargs):
        print("user passed test", owner_wrapper_func)
        return super().dispatch(*args, **kwargs)



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
                users = user_creation_form.save()
                profile = profile_form.save(commit=False)
                profile.user = users
                profile.save()
                return redirect('restaurant_app:login')
            except:
                return render_to_response("registration/create_user.html",
                                      {'u_form': UserCreationForm, 'p_form': ProfileForm},
                                      context_instance=RequestContext(request))
    return render_to_response("registration/create_user.html",
                                  {'u_form': UserCreationForm, 'p_form': ProfileForm},
                                  context_instance=RequestContext(request))


def permission_denied(requests):
    return render_to_response("restaurant_app/permission_denied.html",
                              context_instance=RequestContext(requests))


@login_required
def activate(requests):
    staff = 'staff'
    owner = 'owner'
    input = requests.POST['auth_code']
    user_id = requests.user.id
    profile = Profile.objects.get(user_id=user_id)
    if input == staff:
        profile.staff = True
    if input == owner:
        profile.owner = True
    else:
        return redirect('restaurant_app:denied')
    profile.save()
    context={'profile': profile}
    return render_to_response("registration/add_permissions.html",context, context_instance=RequestContext(requests))
