from django.urls import path
from django.contrib import admin
from summu.views import summu_dars_jadval


urlpatterns = [
    path('', summu_dars_jadval, name='summu_dars_jadval'),
    path('admin/', admin.site.urls)
]