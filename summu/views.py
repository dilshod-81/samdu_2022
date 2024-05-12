import requests
from datetime import datetime, timezone
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
def grouh_ruyxat(request):
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
def summu_dars_jadval(request):
    groups, unique_faculties = grouh_ruyxat(request)
    headers = {"Authorization": "Bearer WX9JzzBDySW6D--m6F83VJgDH-h5QNq8"}
    base_url = "https://student.sammu.uz/rest/v1/data/schedule-list"
    if request.method == 'POST':
        name_id = request.POST.get('group_select')
        fakul_id = request.POST.get('fakul_id')
        semester_code = request.POST.get('semester_code')
        print(fakul_id)
        print(name_id)

        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        query_params = []
        if start_date and end_date:
            dt = datetime.strptime(start_date, "%Y-%m-%d")
            end_dt = datetime.strptime(end_date, "%Y-%m-%d")

            utc_dt = dt.replace(tzinfo=timezone.utc)
            utc_end_dt = end_dt.replace(tzinfo=timezone.utc)

            timestamp = int(utc_dt.timestamp())
            timestamp_end = int(utc_end_dt.timestamp())
            query_params = []
            if fakul_id:
                query_params.append(f"_faculty={int(fakul_id)}")
            if name_id:
                query_params.append(f"_group={int(name_id)}")
            if timestamp and timestamp_end:
                query_params.append(f"lesson_date_from={timestamp}")
                query_params.append(f"lesson_date_to={timestamp_end}")
            if semester_code:
                query_params.append(f"_semester={semester_code}")

        #Shartga bog'liq qo'shimcha kod
        if query_params:
            url = f"{base_url}?{'&'.join(query_params)}"
            print(url)
        else:
            url = base_url
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
        'groups': groups,
        'faculties': unique_faculties
    }
    return render(request, 'summu_id.html', context)


# Create your views here.
