from django.contrib import admin

# Register your models here.
from restaurants.models import Restaurant, Food, Comment

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone_number', 'address')
	search_fields = ('name', )

class FoodAdmin(admin.ModelAdmin):
	"""docstring for FoodAdmin"""
	list_display = ('name', 'restaurant', 'price')
	list_filter = ('is_spicy',)
	fields =('name', 'price', 'restaurant',)
	ordering = ('-price',)

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Comment)