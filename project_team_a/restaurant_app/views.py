from django.shortcuts import render, render_to_response
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(requests):
    return render_to_response("home.html")

