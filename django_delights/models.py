from django.db import models

# Create your models here.
class Ingredient(models.Model):
    UNIT_CHOICES = (
        ('kg', 'Kilograms'),
        ('g', 'Grams'),
        ('lb', 'Pounds'),
        ('oz', 'Ounces'),
        ('unit', 'Units'),
    )
     
    name = models.CharField(max_length=100, blank=False)
    quantinty = models.CharField(max_length=10, blank=False)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class MenuItem(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantinty = models.FloatField(default=0.0, null=False)

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem)
    time_stamp = models.DateField((""), auto_now=False, auto_now_add=False)