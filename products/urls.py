from django.urls import path
from .views import index, product_info, basket, basket_add, basket_remove, add_favourite, favourites, delete_favourite, product_search, about, contact


urlpatterns = [
    path('', index, name='index'),
    path('filter/<int:category_id>/', index, name='filter'),
    path('product/<int:product_id>/', product_info, name='product_info'),
    path('basket/', basket, name='basket'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('favorites/', favourites, name='favorites_products'),
    path('favorites/add/<int:product_id>/', add_favourite, name='add_favourite'),
    path('favourites/remove/<int:product_id>/', delete_favourite, name='delete_favourite'),
    path('search/', product_search, name='product_search'),
    path('about/', about, name='about'),
    path('contacts/', contact, name='contact')
]
