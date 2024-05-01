from django.contrib import admin
from .models import CategoryModel

#admin.site.register(CategoryModel)

# Register your models here.
@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']