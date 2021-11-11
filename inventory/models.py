from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.forms import ModelForm
# Create your models here.
class Ingredient(models.Model):
    KG = "кг"
    TBSP = "гр"
    OTHER = "другое"
    MEASURE_CHOICES = [
        (KG, "кг"),
        (TBSP, "гр"),
        (OTHER, "другое")
    ]
    name = models.CharField(max_length=30)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=25, choices=MEASURE_CHOICES, default=OTHER)
    unit_price = models.FloatField(default=0)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ingredientlist')

    class Meta:
        ordering = ['name']

class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField(default=0)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('menuitemlist')

    class Meta:
        ordering = ['title']

class RecipeRequirement(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    
    def get_absolute_url(self):
        return reverse('reciperequirementlist')
    
    def __str__(self):
        return str(self.ingredient) + " для " + str(self.menu_item)
    class Meta:
        ordering = ['menu_item']

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)
    
    def __str__(self):
        return str(self.menu_item)

    def get_absolute_url(self):
        return reverse('purchaselist')

    class Meta:
        ordering = ['timestamp']


