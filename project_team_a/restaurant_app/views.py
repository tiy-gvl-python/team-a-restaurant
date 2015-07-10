from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Item

def home(requests):
    return render_to_response("home.html")

class ItemListView(ListView):
    model = Item
    template = "item_list.html"


class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'price']
    success_url = reverse_lazy('restaurant_app:item_list')


class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('restaurant_app:item_list')
