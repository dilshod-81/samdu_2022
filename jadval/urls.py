from django.urls import path

from .views import  ( exchange_rates_view, category_faculty,
                     pediatrya_faculty)
from .views import (pediatriya_ishi_faculty_1, pediatriya_ishi_faculty_2,
                    pediatriya_ishi_faculty_3,pediatriya_ishi_faculty_4,
                    pediatriya_ishi_faculty_5, pediatriya_ishi_faculty_6,
                    davolash_1_faculty_1, davolash_1_faculty_2, davolash_1_faculty_3,
                    davolash_1_faculty_4, davolash_1_faculty_5, davolash_1_faculty_6,
                    davolash_2_faculty_1, davolash_2_faculty_2, davolash_2_faculty_3,
                    davolash_2_faculty_4, davolash_2_faculty_5, davolash_2_faculty_6,
                    
                    tibbiy_pedagok_1_faculty_1, tibbiy_pedagok_1_faculty_2,
                    tibbiy_pedagok_1_faculty_3, tibbiy_pedagok_1_faculty_4,
                    tibbiy_pedagok_1_faculty_5, tibbiy_pedagok_1_faculty_6,
                    oliy_hamshiralik_faculty_4, oliy_hamshiralik_faculty_5, 
                    oliy_hamshiralik_faculty_6, stomatologiya_faculty_1,
                    stomatologiya_faculty_2, stomatologiya_faculty_3,
                    stomatologiya_faculty_4, stomatologiya_faculty_5)
urlpatterns = [
   # path('dars/', sammu_dars_jadval, name='davolash_dars_jadval'),
    path('', category_faculty, name='category'),



    path('pediatriya_1', pediatriya_ishi_faculty_1, name='pediatriya_1_kurs'),
    path('pediatriya_2', pediatriya_ishi_faculty_2, name='pediatriya_2_kurs'),
    path('pediatriya_3', pediatriya_ishi_faculty_3, name='pediatriya_3_kurs'),
    path('pediatriya_4', pediatriya_ishi_faculty_4, name='pediatriya_4_kurs'),
    path('pediatriya_5', pediatriya_ishi_faculty_5, name='pediatriya_5_kurs'),
    path('pediatriya_6', pediatriya_ishi_faculty_6, name='pediatriya_6_kurs'),


    path('davolash-1-1/', davolash_1_faculty_1 , name='davolash_1_kurs_1'),
    path('davolash-1-2/', davolash_1_faculty_2 , name='davolash_1_kurs_2'),
    path('davolash-1-3/', davolash_1_faculty_3, name='davolash_1_kurs_3'),
    path('davolash-1-4/', davolash_1_faculty_4, name='davolash_1_kurs_4'),
    path('davolash-1-5/', davolash_1_faculty_5, name='davolash_1_kurs_5'),
    path('davolash-1-6/', davolash_1_faculty_6, name='davolash_1_kurs_6'),

    path('davolash-2-1/', davolash_2_faculty_1, name='davolash_2_kurs_1'),
    path('davolash-2-2/', davolash_2_faculty_2, name='davolash_2_kurs_2'),
    path('davolash-2-3/', davolash_2_faculty_3, name='davolash_2_kurs_3'),
    path('davolash-2-4/', davolash_2_faculty_4, name='davolash_2_kurs_4'),
    path('davolash-2-5/', davolash_2_faculty_5, name='davolash_2_kurs_5'),
    path('davolash-2-6/', davolash_2_faculty_6, name='davolash_2_kurs_6'),

    path('tibbiy_pedagok-1/', tibbiy_pedagok_1_faculty_1, name='tibbiy_pedagok_1_kurs'),
    path('tibbiy_pedagok-2/', tibbiy_pedagok_1_faculty_2, name='tibbiy_pedagok_2_kurs'),
    path('tibbiy_pedagok-3/', tibbiy_pedagok_1_faculty_3, name='tibbiy_pedagok_3_kurs'),
    path('tibbiy_pedagok-4/', tibbiy_pedagok_1_faculty_4, name='tibbiy_pedagok_4_kurs'),
    path('tibbiy_pedagok-5/', tibbiy_pedagok_1_faculty_5, name='tibbiy_pedagok_5_kurs'),
    path('tibbiy_pedagok-6/', tibbiy_pedagok_1_faculty_6, name='tibbiy_pedagok_6_kurs'),

    path('oliy_hamshiralik-4/', oliy_hamshiralik_faculty_4, name='oliy_hamshiralik_4_kurs'),
    path('oliy_hamshiralik-5/', oliy_hamshiralik_faculty_5, name='oliy_hamshiralik_5_kurs'),
    path('oliy_hamshiralik-6/', oliy_hamshiralik_faculty_6, name='oliy_hamshiralik_6_kurs'),

    path('stomatologiya-1/', stomatologiya_faculty_1, name='stomatologiya_1_kurs'),
    path('stomatologiya-2/', stomatologiya_faculty_2, name='stomatologiya_2_kurs'),
    path('stomatologiya-3/', stomatologiya_faculty_3, name='stomatologiya_3_kurs'),
    path('stomatologiya-4/', stomatologiya_faculty_4, name='stomatologiya_4_kurs'),
    path('stomatologiya-5/', stomatologiya_faculty_5, name='stomatologiya_5_kurs'),



    path('ped/', pediatrya_faculty, name='pediatrya'),
    path('kurs/',exchange_rates_view, name='kurs_valita'),
    #path('dars/', dars_jadval, name='dars_jadval')
    #path('category/<int:id>/', category_detail_page, name='category_detail_page'),

]