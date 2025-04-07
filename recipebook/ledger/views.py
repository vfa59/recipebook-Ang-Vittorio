from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient, RecipeImage
from .forms import RecipeForm, RecipeIngredientForm, NewIngredientForm, RecipeImageForm
from django.forms import formset_factory

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

@login_required
def add_recipe(request):
    IngredientFormSet = formset_factory(RecipeIngredientForm, extra=3)

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        formset = IngredientFormSet(request.POST)

        if recipe_form.is_valid() and formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user  
            recipe.save()
            
            for form in formset:
                if form.cleaned_data:  
                    ingredient = form.save(commit=False)
                    ingredient.recipe = recipe
                    ingredient.save()

            return redirect('ledger:recipes_list')
    
    recipe_form = RecipeForm()
    formset = IngredientFormSet()

    return render(request, 'add_recipe.html', {'recipe_form': recipe_form, 'formset': formset})

@login_required
def create_new_ingredient(request):
    next_url = request.GET.get('next')

    if request.method == 'POST':
        new_ingredient_form = NewIngredientForm(request.POST)
        if new_ingredient_form.is_valid():
            new_ingredient_form.save()

            if next_url:
                return redirect(next_url)
            else:
                return redirect('ledger:add_recipe') 
        
    
    new_ingredient_form = NewIngredientForm()

    return render(request, 'new_ingredient.html', {'new_ingredient_form': new_ingredient_form})

@login_required
def add_recipe_ingredient(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        ingredient_form = RecipeIngredientForm(request.POST)

        if ingredient_form.is_valid():
            new_ingredient = ingredient_form.save(commit=False)
            new_ingredient.recipe = recipe  
            new_ingredient.save()  

            return redirect('ledger:recipe_specific', num=recipe.pk) 

    ingredient_form = RecipeIngredientForm()

    return render(request, 'add_recipe_ingredient.html', {'ingredient_form': ingredient_form, 'recipe': recipe})


@login_required
def add_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe  
            recipe_image.save()
            
            return redirect('ledger:recipe_specific', num=recipe.pk)  
    
    form = RecipeImageForm()

    return render(request, 'add_image.html', {'form': form, 'recipe': recipe})

