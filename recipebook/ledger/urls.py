from django.urls import path
from .views import recipes_list, recipe_specific, home

urlpatterns = [
    path("", home, name="home"),
    path('recipes/list', recipes_list, name="recipes_list"),
    path('recipe/<int:num>/', recipe_specific, name="recipe_specific"),
]

app_name = "ledger"
