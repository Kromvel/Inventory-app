from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from .models import  Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import *

# Create your views here.

def logout_view(request): 
    logout(request)
    return redirect('home')

@login_required
def home(request):
    
    context = {"name": "User", "title": "Главная страница"}
    return render(request, "inventory/home.html", context)

def get_auth(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Loginform(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if form.is_valid() and user is not None:
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("invalid credentials")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Loginform()

    return render(request, 'registration/login.html', {'form': form})



class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"



class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menuitem_list.html"

class RecipeRequirementList(LoginRequiredMixin, ListView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_list.html"

class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create_form.html"
    form_class = IngredientForm

   
    

class MenuItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create_form.html"
    form_class = MenuItemForm
    
class RecipeRequirementCreate(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_create_form.html"
    form_class = RecipeRequirementForm

class PurchaseCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = "inventory/purchase_create_form.html"
    form_class = PurchaseFormOneField

class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update_form.html"
    form_class = IngredientForm

class MenuItemUpdate(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = "inventory/menuitem_update_form.html"
    form_class = MenuItemForm

class RecipeRequirementUpdate(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_update_form.html"
    form_class = RecipeRequirementForm
class PurchaseUpdate(LoginRequiredMixin, UpdateView):
    model = Purchase
    template_name = "inventory/purchase_update_form.html"
    form_class = PurchaseForm

class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"
    success_url = reverse_lazy('ingredientlist')

class MenuItemDelete(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "inventory/menuitem_delete_form.html"
    success_url = reverse_lazy('menuitemlist')

class RecipeRequirementDelete(LoginRequiredMixin, DeleteView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_delete_form.html"
    success_url = reverse_lazy('reciperequirementlist')

class PurchaseDelete(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = "inventory/purchase_delete_form.html"
    success_url = reverse_lazy('purchaselist')


