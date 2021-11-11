"""djangodelights URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventory import views

  

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('accounts/login/', views.get_auth, name="login"),
    path("accounts/logout/", views.logout_view, name="logout"),
    
    path("ingredient/list",views.IngredientList.as_view(), name="ingredientlist"),
    path("menuitem/list",views.MenuItemList.as_view(), name="menuitemlist"),
    path("reciperequirement/list",views.RecipeRequirementList.as_view(), name="reciperequirementlist"),
    path("purchase/list",views.PurchaseList.as_view(), name="purchaselist"),


    path("ingredient/create", views.IngredientCreate.as_view(), name="ingredientcreate"),
    path("menuitem/create", views.MenuItemCreate.as_view(), name="menuitemcreate"),
    path("reciperequirement/create", views.RecipeRequirementCreate.as_view(), name="reciperequirementcreate"),
    path("purchase/create", views.PurchaseCreate.as_view(), name="purchasecreate"),

    path("ingredient/update/<pk>", views.IngredientUpdate.as_view(), name="ingredientupdate"),
    path("menuitem/update/<pk>", views.MenuItemUpdate.as_view(), name="menuitemupdate"),
    path("reciperequirement/update/<pk>", views.RecipeRequirementUpdate.as_view(), name="reciperequirementupdate"),
    path("purchase/update/<pk>", views.PurchaseUpdate.as_view(), name="purchaseupdate"),

    path("ingredient/delete/<pk>", views.IngredientDelete.as_view(), name="ingredientdelete"),
    path("menuitem/delete/<pk>", views.MenuItemDelete.as_view(), name="menuitemdelete"),
    path("reciperequirement/delete/<pk>", views.RecipeRequirementDelete.as_view(), name="reciperequirementdelete"),
    path("purchase/delete/<pk>", views.PurchaseDelete.as_view(), name="purchasedelete"),
]

