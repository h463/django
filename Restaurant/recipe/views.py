# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Recipe, MyUser
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='/recipe/')
def home(request):
    recipes=Recipe.objects.order_by("id")
    return render(request, "home.html", {"recipes": recipes})

def login_view(request):
    if request.method == "POST":
        user = authenticate(email=request.POST["email"],
                            password=request.POST["password"])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/recipe/home")
        else:
            return render(request, "login.html", {"error": "Invalid_Credentials"})
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        MyUser.objects.create_user(email=request.POST["email"],
                                   password=request.POST["password"],
                                   date_of_birth=request.POST["date_of_birth"])
        return HttpResponseRedirect("/recipe/")

    return render(request, "register.html")


def create_recipe(request):
    return render(request,"create_recipe.html")

def save_recipe(request):
    print(request.POST)
    print(request.FILES)
    Recipe.objects.create(name=request.POST["name"],
                          ingredients=request.POST["ingredients"],
                          process=request.POST["process"],
                          image=request.FILES["image"])
    return HttpResponseRedirect("/recipe/home/")

@login_required(login_url='/recipe/')
def detail(request,recipe_id):
    recipe=Recipe.objects.get(pk=recipe_id)
    return render(request,"detail.html",{"recipe":recipe})

@login_required(login_url='/recipe/')
def delete(request,recipe_id):
    Recipe.objects.get(pk=recipe_id).delete()

    return HttpResponseRedirect("/recipe/")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/recipe/home/")


