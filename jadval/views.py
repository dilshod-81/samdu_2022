from django.shortcuts import render
from .models import CategoryModel
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

def sammu_dars_jadval(request):
    # URL dan ma'lumotlarni olish
    # if request.method == 'POST':
    #     name_id = request.POST.get('name_id', None)  # Foydalanuvchi tomonidan kiritilgan guruh ID ni olish
    #     print(name_id)
    #
    #headers = {"Authorization": "Bearer WX9JzzBDySW6D--m6F83VJgDH-h5QNq8"}
    #response = requests.get("https://student.sammu.uz/rest/v1/data/schedule-list", headers=headers)

    if request.method == 'POST':
        name_id = request.POST.get('name_id', None)  # Foydalanuvchi tomonidan kiritilgan guruh ID ni olish
        fakul_id = request.POST.get('fakul_id', None)
        semester_code = request.POST.get('semester_code', None)

        if name_id:
            name_id_n = int(name_id)  # Guruh ID ni integer formatga o'tkazish
            fakul_id_n = int(fakul_id)
            semester_code_n = semester_code
            headers = {"Authorization": "Bearer WX9JzzBDySW6D--m6F83VJgDH-h5QNq8"}
            # APIga qilinadigan so'rov URLini dinamik tarzda formatlash
            response = requests.get(f"https://student.sammu.uz/rest/v1/data/schedule-list?_faculty={fakul_id_n}&_group={name_id_n}&_semester={semester_code_n}",
                                    headers=headers)
        else:
            headers = {"Authorization": "Bearer WX9JzzBDySW6D--m6F83VJgDH-h5QNq8"}
            response = requests.get("https://student.sammu.uz/rest/v1/data/schedule-list", headers=headers)
    else:
        headers = {"Authorization": "Bearer WX9JzzBDySW6D--m6F83VJgDH-h5QNq8"}
        response = requests.get("https://student.sammu.uz/rest/v1/data/schedule-list", headers=headers)
    data = response.json()
    kurs = data['data']['items']

    def timestamp_to_weekday_and_dmy(timestamp):
        from datetime import datetime
        days = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
        weekday = days[datetime.utcfromtimestamp(timestamp).weekday()]
        formatted_date = datetime.utcfromtimestamp(timestamp).strftime('%d.%m.%Y')
        return {'weekday': weekday, 'formatted_date': formatted_date}

    def timestamp_to_dmy(timestamp):
        from datetime import datetime
        return datetime.utcfromtimestamp(timestamp).strftime('%d.%m.%Y')

    # Modify the kurs dictionary by applying the functions
    for dars in kurs:
        lesson_date_info = timestamp_to_weekday_and_dmy(dars['lesson_date'])
        week_start_time_info = timestamp_to_weekday_and_dmy(dars['weekStartTime'])
        week_end_time_info = timestamp_to_weekday_and_dmy(dars['weekEndTime'])

        dars['lesson_date'] = lesson_date_info['weekday']
        dars['lesson_date_formatted'] = lesson_date_info['formatted_date']
        dars['weekStartTime'] = week_start_time_info['weekday']
        dars['weekStartTime_formatted'] = week_start_time_info['formatted_date']
        dars['weekEndTime'] = week_end_time_info['weekday']
        dars['weekEndTime_formatted'] = week_end_time_info['formatted_date']

    sum_age = []
    group_name =[]
    kafedra_name=[]
    group_li=[]
    group_li_id=[]
    for key in kurs:
        faculty = key['faculty']['name']
        kafedra = key['department']['name']
        group = key['group']['name']
        group_id=key['group']['id']
        gr=key['group']
        sum_age.append(faculty)
        kafedra_name.append(kafedra)
        group_name.append(group)
        group_li_id.append(group_id)
        group_li.append(gr)
    fakul=list(set(sum_age))
    kafedra_list=list(set(kafedra_name))
    group_n=list(set(group_name))
    group_n_id=list(set(group_li_id))
    json_strs = [json.dumps(d, sort_keys=True) for d in group_li]
    unique_json_strs = set(json_strs)
    unique_dicts = [json.loads(s) for s in unique_json_strs]

    context = {
        'jadval': kurs,
        'faculty': fakul,
        'group_n': group_n,
        'group_li':unique_dicts,
        'kafedra_list':kafedra_list,
        'group_n_id': group_n_id,

    }
    return render(request, 'dars_jadval.html', context)

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



