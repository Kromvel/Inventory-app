from django import forms
from .models import *



class Loginform(forms.Form):
    username = forms.CharField(max_length= 25,label="Введите имя пользователя")
    password = forms.CharField(max_length= 30, label='Введите пароль', widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(Loginform, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

class IngredientForm(ModelForm):
    
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity','unit','unit_price']
        labels = {
        "name": "Название ингредиента",
        "quantity": "Количество",
        "unit": "СИ",
        "unit_price": "Итоговая стоимость"
    }
    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['unit'].widget.attrs.update({'class': 'form-control'})
        self.fields['unit_price'].widget.attrs.update({'class': 'form-control'})

class MenuItemForm(ModelForm):
    
    class Meta:
        model = MenuItem
        fields = ['title', 'price']
        labels = {
        "title": "Название блюда",
        "price": "Цена",
    }
    def __init__(self, *args, **kwargs):
        super(MenuItemForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})

class RecipeRequirementForm(ModelForm):
    
    class Meta:
        model = RecipeRequirement
        fields = ["ingredient", "menu_item", "quantity"]
        labels = {
        "ingredient": "Название ингредиента",
        "menu_item": "Название блюда",
        "quantity": "Количество",
    }
    def __init__(self, *args, **kwargs):
        super(RecipeRequirementForm, self).__init__(*args, **kwargs)
        self.fields['ingredient'].widget.attrs.update({'class': 'form-control'})
        self.fields['menu_item'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})

class PurchaseForm(ModelForm):
    
    class Meta:
        model = Purchase
        fields = ["menu_item", "timestamp"]
        labels = {
        "menu_item": "Название блюда",
        "timestamp": "Дата и время заказа"
    }
    def __init__(self, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)
        self.fields['menu_item'].widget.attrs.update({'class': 'form-control'})
        self.fields['timestamp'].widget.attrs.update({'class': 'form-control'})

class PurchaseFormOneField(ModelForm):
    
    class Meta:
        model = Purchase
        fields = ["menu_item"]
        labels = {
        "menu_item": "Название блюда"

    }
    def __init__(self, *args, **kwargs):
        super(PurchaseFormOneField, self).__init__(*args, **kwargs)
        self.fields['menu_item'].widget.attrs.update({'class': 'form-control'})


