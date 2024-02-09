from django.contrib import admin
from .models import Categories, Orders


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ( 'nickname', 'age', 'description', 'owner')
    list_display_links = ('id', 'date_of_order', 'categories', 'nickname', 'age', 'description', 'owner')
