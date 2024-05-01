from django.urls import path
from django.contrib import admin
from .views import category_detail_page, sammu_dars_jadval, exchange_rates_view

urlpatterns = [
    path('dars/', sammu_dars_jadval, name='sammu_dars_jadval'),
    path('kurs/',exchange_rates_view, name='kurs_valita'),
    path('admin/', admin.site.urls)
    #path('dars/', dars_jadval, name='dars_jadval')
    #path('category/<int:id>/', category_detail_page, name='category_detail_page'),

]