from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Recipe


def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes_list.html', {'recipes': recipes})


def recipe_specific(request, num):   
    try:
        recipe = Recipe.objects.get(id=num)
    except Recipe.DoesNotExist:
        return HttpResponseNotFound("Recipe does not exist.")
    
    ingredients = recipe.ingredients.all()
    return render(request, 'recipe_specific.html', {'recipe':recipe, 'ingredients': ingredients})
