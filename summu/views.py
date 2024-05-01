import requests
from datetime import datetime
from django.shortcuts import render
import json
import requests
def get_api_response(endpoint, headers):
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None  # Or return a default structure that your code can handle

def timestamp_to_weekday_and_dmy(timestamp):
    days = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
    weekday = days[datetime.utcfromtimestamp(timestamp).weekday()]
    formatted_date = datetime.utcfromtimestamp(timestamp).strftime('%d.%m.%Y')
    return {'weekday': weekday, 'formatted_date': formatted_date}

def summu_dars_jadval(request):
    headers = {"Authorization": "Bearer WX9JzzBDySW6D--m6F83VJgDH-h5QNq8"}
    base_url = "https://student.sammu.uz/rest/v1/data/schedule-list"

    if request.method == 'POST':
        name_id = request.POST.get('name_id')
        fakul_id =request.POST.get('fakul_id')
        semester_code =request.POST.get('semester_code')

        print(fakul_id)
        print(name_id)
        print(semester_code)
        query_params = []
        if name_id and fakul_id:
            query_params.append(f"_faculty={int(fakul_id)}")
            query_params.append(f"_group={int(name_id)}")
        if semester_code:
            query_params.append(f"_semester={semester_code}")
        url = f"{base_url}?{'&'.join(query_params)}" if query_params else base_url
    else:
        url = base_url

    data = get_api_response(url, headers)

    if data is None:
        kurs = []
    else:
        kurs = data['data']['items']

        for dars in kurs:
            dars.update({
                'lesson_date': timestamp_to_weekday_and_dmy(dars['lesson_date']),
                'weekStartTime': timestamp_to_weekday_and_dmy(dars['weekStartTime']),
                'weekEndTime': timestamp_to_weekday_and_dmy(dars['weekEndTime'])
            })

    unique_groups = {json.dumps(k['group'], sort_keys=True) for k in kurs}
    unique_facults = {json.dumps(k['faculty'], sort_keys=True) for k in kurs}
    unique_semester = {json.dumps(k['semester'], sort_keys=True) for k in kurs}

    unique_date = {json.dumps(k['lesson_date'], sort_keys=True) for k in kurs}


    group_list = [json.loads(g) for g in unique_groups]
    fakul_list = [json.loads(g) for g in unique_facults]
    semester_list = [json.loads(g) for g in unique_semester]
    lesson_time = [json.loads(g) for g in unique_date]

    context = {
        'jadval': kurs,
        'faculty': list({k['faculty']['name'] for k in kurs}),
        'group_n': list({k['group']['name'] for k in kurs}),
        'group_li': group_list,
        'fakul_list': fakul_list,
        'semester_list': semester_list,
        'unique_date': lesson_time,
        'kafedra_list': list({k['department']['name'] for k in kurs}),
        'group_n_id': list({k['group']['id'] for k in kurs}),
    }
    return render(request, 'summu.html', context)


# Create your views here.
