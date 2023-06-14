from django.http import JsonResponse
from .utils import percentofAfricanAmericanStudents, getData, sort_statistics


def schoolRank(request):
    state_abr_list = \
        ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
         'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
         'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
         'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
         'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', ]

    content = []
    statistics_ = []

    for state in state_abr_list:
        content.append([state, getData(state)])

    for data in content:
        state = data[0]
        schoolList = data[1]
        statistics_.append(
            list(percentofAfricanAmericanStudents(state, schoolList, [2018]).items()))

    keys = request.GET.keys()
    params={}
    if len(keys) > 0:
        if 'top' in keys:
            params['top'] = request.GET['top']
        if 'column_name' in keys:
            params['column_name'] = request.GET['column_name']


    sorted_list = sort_statistics(statistics_, params)

    return JsonResponse(sorted_list, safe=False, json_dumps_params={'indent': 2})
