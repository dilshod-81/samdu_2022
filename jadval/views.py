from tokenize import group
from django.shortcuts import render
from .models import CategoryModel, PediatryaModel
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import json
import requests


def category_detail_page(request, id):

    category_context = CategoryModel.objects.get(id=id)
    template = loader.get_template('news/category_detail.html')
    context = {
        "category_context": category_context,


    }
    return HttpResponse(template.render(context, request))

def category_faculty(request):
    category_context = CategoryModel.objects.all()
    template = loader.get_template('faculty.html')
    context = {
        "category_context": category_context,
    }
    return HttpResponse(template.render(context, request))

def pediatrya_faculty(request):
    pediatrya_fac=PediatryaModel.objects.all()
    template = loader.get_template('pediatrya.html')
    with open('fayl/fakultetlar.json') as f:
        data = json.load(f)
    kurs = data['data']['items']
    context = {
        "pediatrya_fac": pediatrya_fac,
        'kurs': kurs
    }
    return HttpResponse(template.render(context, request))

def pediatriya_ishi_faculty(request):
    with open('fayl/pediatriya_ishi_fac.json') as f:
        data = json.load(f)
        kurslar = {
            'kurs_1': data['Pediatriya ishi']['1-kurs'],
            'kurs_2': data['Pediatriya ishi']['2-kurs'],
            'kurs_3': data['Pediatriya ishi']['3-kurs'],
            'kurs_4': data['Pediatriya ishi']['4-kurs'],
            'kurs_5': data['Pediatriya ishi']['5-kurs'],
            'kurs_6': data['Pediatriya ishi']['6-kurs']
        }
    return kurslar




def pediatriya_ishi_faculty_1(request):
    kurslar = pediatriya_ishi_faculty(request)
    kurs_1 = kurslar['kurs_1']
    template = loader.get_template('pediatriya_ishi/pediatriya_1_kurs.html')
    context = {
        'kurs_1': kurs_1,
    }
    return HttpResponse(template.render(context, request))
def pediatriya_ishi_faculty_2(request):
    kurslar = pediatriya_ishi_faculty(request)
    kurs_2 = kurslar['kurs_2']
    template = loader.get_template('pediatriya_ishi/pediatriya_2_kurs.html')
    context = {

        'kurs_2': kurs_2,
    }
    return HttpResponse(template.render(context, request))
def pediatriya_ishi_faculty_3(request):
    kurslar = pediatriya_ishi_faculty(request)
    kurs_3 = kurslar['kurs_3']
    template = loader.get_template('pediatriya_ishi/pediatriya_3_kurs.html')
    context = {
        'kurs_3': kurs_3,
    }
    return HttpResponse(template.render(context, request))

def pediatriya_ishi_faculty_4(request):
    kurslar = pediatriya_ishi_faculty(request)
    kurs_4 = kurslar['kurs_4']
    template = loader.get_template('pediatriya_ishi/pediatriya_4_kurs.html')
    context = {
        'kurs_4': kurs_4,
    }
    return HttpResponse(template.render(context, request))

def pediatriya_ishi_faculty_5(request):
    kurslar = pediatriya_ishi_faculty(request)
    kurs_5 = kurslar['kurs_5']
    template = loader.get_template('pediatriya_ishi/pediatriya_5_kurs.html')
    context = {
        'kurs_5': kurs_5,
    }
    return HttpResponse(template.render(context, request))

def pediatriya_ishi_faculty_6(request):
    kurslar = pediatriya_ishi_faculty(request)
    kurs_6 = kurslar['kurs_6']
    template = loader.get_template('pediatriya_ishi/pediatriya_6_kurs.html')
    context = {
        'kurs_6': kurs_6,
    }
    return HttpResponse(template.render(context, request))

def davolash_1_faculty(request):
    with open('fayl/davolash_1_fac.json') as f:
        data = json.load(f)
        kurslar = {
            'kurs_1': data['1-son Davolash ishi']['1-kurs'],
            'kurs_2': data['1-son Davolash ishi']['2-kurs'],
            'kurs_3': data['1-son Davolash ishi']['3-kurs'],
            'kurs_4': data['1-son Davolash ishi']['4-kurs'],
            'kurs_5': data['1-son Davolash ishi']['5-kurs'],
            'kurs_6': data['1-son Davolash ishi']['6-kurs']
        }
    return kurslar
def davolash_1_faculty_1(request):
    kurslar = davolash_1_faculty(request)
    kurs_1 = kurslar['kurs_1']
    template = loader.get_template('davolash-1/davolash_1_kurs_1.html')
    context = {
        'kurs_1': kurs_1,
    }
    return HttpResponse(template.render(context, request))

def davolash_1_faculty_2(request):
    kurslar = davolash_1_faculty(request)
    kurs_2 = kurslar['kurs_2']
    template = loader.get_template('davolash-1/davolash_1_kurs_2.html')
    context = {
        'kurs_2': kurs_2,
    }
    return HttpResponse(template.render(context, request))

def davolash_1_faculty_3(request):
    kurslar = davolash_1_faculty(request)
    kurs_3 = kurslar['kurs_3']
    template = loader.get_template('davolash-1/davolash_1_kurs_3.html')
    context = {
        'kurs_3': kurs_3,
    }
    return HttpResponse(template.render(context, request))

def davolash_1_faculty_4(request):
    kurslar = davolash_1_faculty(request)
    kurs_4 = kurslar['kurs_4']
    template = loader.get_template('davolash-1/davolash_1_kurs_4.html')
    context = {
        'kurs_4': kurs_4,
    }
    return HttpResponse(template.render(context, request))

def davolash_1_faculty_5(request):
    kurslar = davolash_1_faculty(request)
    kurs_5 = kurslar['kurs_5']
    template = loader.get_template('davolash-1/davolash_1_kurs_5.html')
    context = {
        'kurs_5': kurs_5,
    }
    return HttpResponse(template.render(context, request))
def davolash_1_faculty_6(request):
    kurslar = davolash_1_faculty(request)
    kurs_6 = kurslar['kurs_6']
    template = loader.get_template('davolash-1/davolash_1_kurs_6.html')
    context = {
        'kurs_6': kurs_6,
    }
    return HttpResponse(template.render(context, request))


def davolash_2_faculty(request):
    with open('fayl/davolash_2_fac.json') as f:
        data = json.load(f)
        kurslar = {
            'kurs_1': data['2-son Davolash ishi']['1-kurs'],
            'kurs_2': data['2-son Davolash ishi']['2-kurs'],
            'kurs_3': data['2-son Davolash ishi']['3-kurs'],
            'kurs_4': data['2-son Davolash ishi']['4-kurs'],
            'kurs_5': data['2-son Davolash ishi']['5-kurs'],
            'kurs_6': data['2-son Davolash ishi']['6-kurs']
        }
    return kurslar

def davolash_2_faculty_1(request):
    kurslar = davolash_2_faculty(request)
    kurs_1 = kurslar['kurs_1']
    template = loader.get_template('davolash-2/davolash_2_kurs_1.html')
    context = {
        'kurs_1': kurs_1,
    }
    return HttpResponse(template.render(context, request))

def davolash_2_faculty_2(request):
    kurslar = davolash_2_faculty(request)
    kurs_2 = kurslar['kurs_2']
    template = loader.get_template('davolash-2/davolash_2_kurs_2.html')
    context = {
        'kurs_2': kurs_2,
    }
    return HttpResponse(template.render(context, request))

def davolash_2_faculty_3(request):
    kurslar = davolash_2_faculty(request)
    kurs_3 = kurslar['kurs_3']
    template = loader.get_template('davolash-2/davolash_2_kurs_3.html')
    context = {
        'kurs_3': kurs_3,
    }
    return HttpResponse(template.render(context, request))

def davolash_2_faculty_4(request):
    kurslar = davolash_2_faculty(request)
    kurs_4 = kurslar['kurs_4']
    template = loader.get_template('davolash-2/davolash_2_kurs_4.html')
    context = {
        'kurs_4': kurs_4,
    }
    return HttpResponse(template.render(context, request))

def davolash_2_faculty_5(request):
    kurslar = davolash_2_faculty(request)
    kurs_5 = kurslar['kurs_5']
    template = loader.get_template('davolash-2/davolash_2_kurs_5.html')
    context = {
        'kurs_5': kurs_5,
    }
    return HttpResponse(template.render(context, request))

def davolash_2_faculty_6(request):
    kurslar = davolash_2_faculty(request)
    kurs_6 = kurslar['kurs_6']
    template = loader.get_template('davolash-2/davolash_2_kurs_6.html')
    context = {
        'kurs_6': kurs_6,
    }
    return HttpResponse(template.render(context, request))

def group_list(request):
    # URL dan ma'lumotlarni olish
    headers = {"Authorization": "Bearer WX9JzzBDySW6D--m6F83VJgDH-h5QNq8"}
    data = []
    for page in range(1, 10):
        response = requests.get(f"https://student.sammu.uz/rest/v1/data/group-list?page={page}&limit=200",
                                headers=headers)
        if response.status_code == 200:
            page_data = response.json()
            data.extend(page_data['data']['items'])
        else:
            print(f"Error fetching data for page {page}: {response.status_code}")

    # Fakultetlarni olish
    faculties = [group['department'] for group in data]

    # Unikal fakultetlarni tanlash
    unique_faculties = list({json.dumps(faculty, sort_keys=True): faculty for faculty in faculties}.values())

    # Ma'lumotlarni va unikal fakultetlarni qaytarish
    return data, unique_faculties


def tibbiy_pedagok_1_faculty_1(request):
    # group_list funksiyasidan ma'lumotlarni olamiz
    groups, unique_faculties = group_list(request)
    
    # Template va context tayyorlash
    template = loader.get_template('tibbiy_pedogogika/tibbiy_pedogogika_1_kurs_1.html')
    context = {
        'groups': groups,
        'faculties': unique_faculties
    }

    return HttpResponse(template.render(context, request))

def tibbiy_pedagok_1_faculty_2(request):
    # group_list funksiyasidan ma'lumotlarni olamiz
    groups, unique_faculties = group_list(request)
    
    # Template va context tayyorlash
    template = loader.get_template('tibbiy_pedogogika/tibbiy_pedogogika_1_kurs_2.html')
    context = {
        'groups': groups,
        'faculties': unique_faculties
    }

    return HttpResponse(template.render(context, request))

def tibbiy_pedagok_1_faculty_3(request):
    # group_list funksiyasidan ma'lumotlarni olamiz
    groups, unique_faculties = group_list(request)
    
    # Template va context tayyorlash
    template = loader.get_template('tibbiy_pedogogika/tibbiy_pedogogika_1_kurs_3.html')
    context = {
        'groups': groups,
        'faculties': unique_faculties
    }

    return HttpResponse(template.render(context, request))

def tibbiy_pedagok_1_faculty_4(request):
    # group_list funksiyasidan ma'lumotlarni olamiz
    groups, unique_faculties = group_list(request)
    
    # Template va context tayyorlash
    template = loader.get_template('tibbiy_pedogogika/tibbiy_pedogogika_1_kurs_4.html')
    context = {
        'groups': groups,
        'faculties': unique_faculties
    }

    return HttpResponse(template.render(context, request))

def tibbiy_pedagok_1_faculty_5(request):
    # group_list funksiyasidan ma'lumotlarni olamiz
    groups, unique_faculties = group_list(request)
    
    # Template va context tayyorlash
    template = loader.get_template('tibbiy_pedogogika/tibbiy_pedogogika_1_kurs_5.html')
    context = {
        'groups': groups,
        'faculties': unique_faculties
    }

    return HttpResponse(template.render(context, request))

def tibbiy_pedagok_1_faculty_6(request):
    # group_list funksiyasidan ma'lumotlarni olamiz
    groups, unique_faculties = group_list(request)
    
    # Template va context tayyorlash
    template = loader.get_template('tibbiy_pedogogika/tibbiy_pedogogika_1_kurs_6.html')
    context = {
        'groups': groups,
        'faculties': unique_faculties
    }

    return HttpResponse(template.render(context, request))



def oliy_hamshiralik_faculty_4(request):
    # group_list funksiyasidan ma'lumotlarni olamiz
    groups, unique_faculties = group_list(request)
    
    # Template va context tayyorlash
    template = loader.get_template('oliy_hamshiralik_ish/oliy_hamshiralik_kurs_4.html')
    context = {
        'groups': groups,
        'faculties': unique_faculties
    }

    return HttpResponse(template.render(context, request))

def oliy_hamshiralik_faculty_5(request):
    # group_list funksiyasidan ma'lumotlarni olamiz
    groups, unique_faculties = group_list(request)
    
    # Template va context tayyorlash
    template = loader.get_template('oliy_hamshiralik_ish/oliy_hamshiralik_kurs_5.html')
    context = {
        'groups': groups,
        'faculties': unique_faculties
    }

    return HttpResponse(template.render(context, request))

def oliy_hamshiralik_faculty_6(request):
    # group_list funksiyasidan ma'lumotlarni olamiz
    groups, unique_faculties = group_list(request)
    # Template va context tayyorlash
    template = loader.get_template('oliy_hamshiralik_ish/oliy_hamshiralik_kurs_6.html')
    context = {
        'groups': groups,
        'faculties': unique_faculties
    }
    return HttpResponse(template.render(context, request))

def stomatologiya_faculty_1(request):
    # group_list funksiyasidan ma'lumotlarni olamiz
    groups, unique_faculties = group_list(request)
    # Template va context tayyorlash
    template = loader.get_template('stomatologiya/stomatologiya_1_kurs.html')
    context = {
        'groups': groups,
        'faculties': unique_faculties
    }
    return HttpResponse(template.render(context, request))
def stomatologiya_faculty_2(request):
    # group_list funksiyasidan ma'lumotlarni olamiz
    groups, unique_faculties = group_list(request)
    # Template va context tayyorlash
    template = loader.get_template('stomatologiya/stomatologiya_2_kurs.html')
    context = {
        'groups': groups,
        'faculties': unique_faculties
    }
    return HttpResponse(template.render(context, request))

def stomatologiya_faculty_3(request):
    # group_list funksiyasidan ma'lumotlarni olamiz
    groups, unique_faculties = group_list(request)
    # Template va context tayyorlash
    template = loader.get_template('stomatologiya/stomatologiya_3_kurs.html')
    context = {
        'groups': groups,
        'faculties': unique_faculties
    }
    return HttpResponse(template.render(context, request))

def stomatologiya_faculty_4(request):
    # group_list funksiyasidan ma'lumotlarni olamiz
    groups, unique_faculties = group_list(request)
    # Template va context tayyorlash
    template = loader.get_template('stomatologiya/stomatologiya_4_kurs.html')
    context = {
        'groups': groups,
        'faculties': unique_faculties
    }
    return HttpResponse(template.render(context, request))

def stomatologiya_faculty_5(request):
    # group_list funksiyasidan ma'lumotlarni olamiz
    groups, unique_faculties = group_list(request)
    # Template va context tayyorlash
    template = loader.get_template('stomatologiya/stomatologiya_5_kurs.html')
    context = {
        'groups': groups,
        'faculties': unique_faculties
    }
    return HttpResponse(template.render(context, request))














# def sammu_dars_jadval(request):
#
#     if request.method == 'POST':
#         name_id = request.POST.get('name_id', None)  # Foydalanuvchi tomonidan kiritilgan guruh ID ni olish
#         fakul_id = request.POST.get('fakul_id', None)
#         semester_code = request.POST.get('semester_code', None)
#
#         if name_id:
#             name_id_n = int(name_id)  # Guruh ID ni integer formatga o'tkazish
#             fakul_id_n = int(fakul_id)
#             semester_code_n = semester_code
#             headers = {"Authorization": "Bearer WX9JzzBDySW6D--m6F83VJgDH-h5QNq8"}
#             # APIga qilinadigan so'rov URLini dinamik tarzda formatlash
#             response = requests.get(f"https://student.sammu.uz/rest/v1/data/schedule-list?_faculty={fakul_id_n}&_group={name_id_n}&_semester={semester_code_n}",
#                                     headers=headers)
#         else:
#             headers = {"Authorization": "Bearer WX9JzzBDySW6D--m6F83VJgDH-h5QNq8"}
#             response = requests.get("https://student.sammu.uz/rest/v1/data/schedule-list", headers=headers)
#     else:
#         headers = {"Authorization": "Bearer WX9JzzBDySW6D--m6F83VJgDH-h5QNq8"}
#         response = requests.get("https://student.sammu.uz/rest/v1/data/schedule-list", headers=headers)
#     data = response.json()
#     kurs = data['data']['items']
#
#     def timestamp_to_weekday_and_dmy(timestamp):
#         from datetime import datetime
#         days = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
#         weekday = days[datetime.utcfromtimestamp(timestamp).weekday()]
#         formatted_date = datetime.utcfromtimestamp(timestamp).strftime('%d.%m.%Y')
#         return {'weekday': weekday, 'formatted_date': formatted_date}
#
#     def timestamp_to_dmy(timestamp):
#         from datetime import datetime
#         return datetime.utcfromtimestamp(timestamp).strftime('%d.%m.%Y')
#
#     # Modify the kurs dictionary by applying the functions
#     for dars in kurs:
#         lesson_date_info = timestamp_to_weekday_and_dmy(dars['lesson_date'])
#         week_start_time_info = timestamp_to_weekday_and_dmy(dars['weekStartTime'])
#         week_end_time_info = timestamp_to_weekday_and_dmy(dars['weekEndTime'])
#
#         dars['lesson_date'] = lesson_date_info['weekday']
#         dars['lesson_date_formatted'] = lesson_date_info['formatted_date']
#         dars['weekStartTime'] = week_start_time_info['weekday']
#         dars['weekStartTime_formatted'] = week_start_time_info['formatted_date']
#         dars['weekEndTime'] = week_end_time_info['weekday']
#         dars['weekEndTime_formatted'] = week_end_time_info['formatted_date']
#
#     sum_age = []
#     group_name =[]
#     kafedra_name=[]
#     group_li=[]
#     group_li_id=[]
#     for key in kurs:
#         faculty = key['faculty']['name']
#         kafedra = key['department']['name']
#         group = key['group']['name']
#         group_id=key['group']['id']
#         gr=key['group']
#         sum_age.append(faculty)
#         kafedra_name.append(kafedra)
#         group_name.append(group)
#         group_li_id.append(group_id)
#         group_li.append(gr)
#     fakul=list(set(sum_age))
#     kafedra_list=list(set(kafedra_name))
#     group_n=list(set(group_name))
#     group_n_id=list(set(group_li_id))
#     json_strs = [json.dumps(d, sort_keys=True) for d in group_li]
#     unique_json_strs = set(json_strs)
#     unique_dicts = [json.loads(s) for s in unique_json_strs]
#
#     context = {
#         'jadval': kurs,
#         'faculty': fakul,
#         'group_n': group_n,
#         'group_li':unique_dicts,
#         'kafedra_list':kafedra_list,
#         'group_n_id': group_n_id,
#
#     }
#     return render(request, 'dars_jadval.html', context)

def exchange_rates_view(request):
    # Create an instance of CategoryModel
    category = CategoryModel.objects.create(name="Exchange Rates")
    
    # Fetch exchange rates using the model method
    exchange_rates = category.fetch_exchange_rates()
    # Pass the exchange rates data to the template
    context = {
        'exchange_rates': exchange_rates
    }
    return render(request, 'exchange_rates.html', context)

# views.py



# def dars_jadval(request):
#     if request.method == 'POST':
#         name_id = request.POST.get('name_id', None)  # Foydalanuvchi tomonidan kiritilgan guruh ID ni olish
#         if name_id:  # Agar guruh ID mavjud bo'lsa
#             return render(request, 'exchange_rates.html', {'name_id': name_id})
#     return render(request, 'dars_jadval.html', {'name_id': None})



