from django import template
from ..models import  Ingredient, MenuItem, RecipeRequirement, Purchase

register = template.Library()

@register.simple_tag
def get_sum_purchase():
    purchase = Purchase.objects.select_related('menu_item').all()
    menu = MenuItem.objects.all()
    price_purchase_list=[]
    for m in menu:
        for p in purchase:
            if m.title == str(p.menu_item):
                price_purchase_list.append(m.price)
    price_purchase_sum = sum(price_purchase_list)
    return price_purchase_sum

@register.simple_tag
def get_sum_ingredient():
    ingredients = Ingredient.objects.all()
    ing_price_list = []
    for i in ingredients:
        ing_price_list.append(i.unit_price)
    ing_price_sum = sum(ing_price_list)
    return ing_price_sum

@register.simple_tag
def get_profit():
    sum_ingredient = get_sum_ingredient()
    sum_purchase = get_sum_purchase()
    profit = sum_purchase - sum_ingredient
    return profit