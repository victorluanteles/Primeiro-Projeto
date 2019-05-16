from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("listar", mostrarPokemons, name="listar_pokemons"),
    path("mostrar", mostrarPokemon, name="mostrar_pokemon"),
    path("categoria/criar/", salvarCategoria, name="nova_categoria"),
]
