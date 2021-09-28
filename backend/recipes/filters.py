from django_filters.rest_framework import FilterSet, filters
from rest_framework.filters import SearchFilter

from .models import Recipe, User


class IngredientNameFilter(SearchFilter):
    search_param = 'name'


class RecipeFilter(FilterSet):
    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')
    authot = filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Recipe
        fields = ('author', 'tags')
