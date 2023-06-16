from django.http import JsonResponse
from .utils import percentofAfricanAmericanStudents, getData, sort_statistics


async def schoolRank(request):
    state_abr_list = \
        ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
         'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
         'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
         'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
         'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC']

    statistics_ = []

    keys = request.GET.keys()
    params = {'year': 2018}

    if len(keys) > 0:
        if 'top' in keys and request.GET['top']:
            params['top'] = request.GET['top']
        if 'column_name' in keys and request.GET['column_name']:
            params['column_name'] = request.GET['column_name']
        if 'year' in keys and request.GET['year']:
            params['year'] = [eval(i) for i in request.GET['year'].split(',')]

    content = await getData(state_abr_list)

    for data in content:
        state = data[0]
        schoolList = data[1]
        statistics_.append(
            list(percentofAfricanAmericanStudents(state, schoolList, params['year']).items()))

    sorted_list = sort_statistics(statistics_, params)

    return JsonResponse(sorted_list, safe=False, json_dumps_params={'indent': 2})
