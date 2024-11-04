from django.contrib import admin
from .models import Categories, Products, ProductImage, ProductColor, Basket, FavouriteProduct, Subcategory

admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(ProductImage)
admin.site.register(ProductColor)
admin.site.register(Basket)
admin.site.register(FavouriteProduct)
admin.site.register(Subcategory)
