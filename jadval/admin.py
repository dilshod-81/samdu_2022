from django.contrib import admin
from .models import CategoryModel, PediatryaModel

#admin.site.register(CategoryModel)

# Register your models here.
@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(PediatryaModel)
class PediartyaAdmin(admin.ModelAdmin):
    list_display = [ 'faculty',
                    'id',
                    'kurs_1',
                    'kurs_2',
                    'kurs_3',
                    'kurs_4',
                    'kurs_5',
                    'kurs_6'
                    ]