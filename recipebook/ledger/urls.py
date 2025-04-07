from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('recipes/list', views.recipes_list, name="recipes_list"),
    path('recipe/<int:num>/', views.recipe_specific, name="recipe_specific"),
    path('recipe/add/', views.add_recipe, name='add_recipe'),
    path('recipe/add/new_ingredient', views.create_new_ingredient, name='create_new_ingredient'),
    path('recipes/<int:pk>/add_ingredient/', views.add_recipe_ingredient, name='add_recipe_ingredient'),
    path('recipe/<int:pk>/add_image/', views.add_image, name='add_image'),
]



app_name = "ledger"
