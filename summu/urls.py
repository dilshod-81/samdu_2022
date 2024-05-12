from django.urls import path

from summu.views import summu_dars_jadval


urlpatterns = [
    path('class_schedule/', summu_dars_jadval, name='summu_dars_jadval'),
]