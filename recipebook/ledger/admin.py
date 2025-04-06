from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage, Profile


class RecipeIngredientInline(admin.TabularInline):  
    model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):  
    model = RecipeImage

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    search_fields = ('name', )

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    search_fields = ('name', )
    inlines = [RecipeIngredientInline, RecipeImageInline] 

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

    list_display = ('recipe', 'quantity', 'ingredient',)
    list_filter = ('recipe', )
    search_fields = ('ingredient__name', )

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
