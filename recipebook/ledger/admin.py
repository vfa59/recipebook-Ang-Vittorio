from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):  
    model = RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    search_fields = ('name', )

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    search_fields = ('name', )
    inlines = [RecipeIngredientInline] 

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

    list_display = ('recipe', 'quantity', 'ingredient',)
    list_filter = ('recipe', )
    search_fields = ('ingredient__name', )

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
