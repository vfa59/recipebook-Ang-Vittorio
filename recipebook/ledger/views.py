from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .models import Recipe

@login_required
def home(request):
    return render(request, 'base.html')

@login_required
def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes_list.html', {'recipes': recipes})

@login_required
def recipe_specific(request, num):   
    try:
        recipe = Recipe.objects.get(id=num)
    except Recipe.DoesNotExist:
        return HttpResponseNotFound("Recipe does not exist.")
    
    ingredients = recipe.ingredients.all()
    return render(request, 'recipe_specific.html', {'recipe':recipe, 'ingredients': ingredients})
