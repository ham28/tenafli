from Backend.utils import getData, percentofAfricanAmericanStudents, sort_statistics


def main():

    # directory = 'data/'
    # for filename in os.listdir(directory):
    #     file_path = os.path.join(directory, filename)
    #     if os.path.isfile(file_path):
    #         with open(file_path, 'r') as file:
    #             content = json.load(file)
    #         statistics_.append(list(percentofAfricanAmericanStudents(filename[:-5], content, [2023, 2022, 2021, 2020]).items()))
    #
    #
    # sorted = sort_statistics(statistics_)
    #
    # for row in sorted:
    #     print(row)


    state_abr_list = \
        ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY'
            , 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND'
            , 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC']


    import time

    content = []
    statistics_ = []

    start = time.time()

    for state in state_abr_list:
        content.append([state, getData(state)])

    for data in content:
        state = data[0]
        schoolList = data[1]
        statistics_.append(
            list(percentofAfricanAmericanStudents(state, schoolList, 2020).items()))

    sorted_list = sort_statistics(statistics_)

    for row in sorted_list:
        print(row)

    end = time.time()
    print(end - start)

    # import json
    #
    # with open('data.json', 'w') as f:
    #     json.dump(data, f)
    #
    # sorted_list = sort_statistics(statistics_)
    #
    # print(type(sorted_list))
    # print(sorted_list)
    #
    # for row in sorted_list:
    #     print(row)

    return


if __name__ == '__main__':
    main()
