import asyncio
import time

from Backend.utils import getData, percentofAfricanAmericanStudents, sort_statistics


async def main():

    state_abr_list = \
        ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY'
            , 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND'
            , 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC']

    content = []
    statistics_ = []
    s = time.perf_counter()

    responses = await getData(state_abr_list)

    elapsed = time.perf_counter() - s

    for data in responses:
        state = data[0]
        schoolList = data[1]
        statistics_.append(
            list(percentofAfricanAmericanStudents(state, schoolList, 2020).items()))

    sorted_list = sort_statistics(statistics_)

    for row in sorted_list:
        print(row)


    return


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
