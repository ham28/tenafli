import os
import requests
import datetime
import json


# Compute the Number(Value) associated with a percentage given the totalNumber
def computeNumberFromPercentage(totalNumber, percentage):
    return round(percentage * (totalNumber / 100))


# Compute the Percentage of Number given the totalNumber
def computePercentageFromNumber(totalNumber, number):
    return (number / totalNumber) * 100


# Retrieve Data from API url
# Params (STR)Abreviation of State, (STR)AppID, (STR)appKey, (INT)number of object perPage
def getData(stateAbr, appID='052d9b7b', appKey='2bb041493517101dba0e91f04aee75b0', perPage=20):
    url = 'https://api.schooldigger.com/v2.0/schools?st=' + stateAbr + '&perPage=' + str(
        perPage) + '&appID=' + appID + '&appKey=' + appKey
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return False


# Compute the Percentage
# Params (STR) Abreviation of State, (Json)data associated with the state, (INT, [INT])year can be list of int
def percentofAfricanAmericanStudents(stateAbr, data, year=datetime.date.today().year, is_list=False):
    if type(year) in (list, tuple, dict): is_list = True

    try:
        if data:
            totalStudent = 0
            totalAfricanAmericanStudent = 0

            for school in data['schoolList']:

                try:
                    schoolYearlyDetails = school['schoolYearlyDetails']

                    for schoolYearlyDetail in schoolYearlyDetails:

                        if is_list:
                            if schoolYearlyDetail['year'] in year:
                                numberOfStudents = schoolYearlyDetail['numberOfStudents']
                                totalStudent += numberOfStudents
                                numberOfAfricanAmericanStudents = computeNumberFromPercentage(numberOfStudents,
                                                                                              schoolYearlyDetail[
                                                                                                  'percentofAfricanAmericanStudents'])
                                totalAfricanAmericanStudent += numberOfAfricanAmericanStudents

                        else:
                            if schoolYearlyDetail['year'] == year:
                                numberOfStudents = schoolYearlyDetail['numberOfStudents']
                                totalStudent += numberOfStudents
                                numberOfAfricanAmericanStudents = computeNumberFromPercentage(numberOfStudents,
                                                                                              schoolYearlyDetail[
                                                                                                  'percentofAfricanAmericanStudents'])
                                totalAfricanAmericanStudent += numberOfAfricanAmericanStudents


                except:
                    pass

            return {
                'state': stateAbr,
                'statistic': {
                    'totalStudent': totalStudent,
                    'totalofAfricanAmericanStudents': totalAfricanAmericanStudent,
                    'percentofAfricanAmericanStudents': computePercentageFromNumber(totalStudent,
                                                                                    totalAfricanAmericanStudent)
                }
            }

    except Exception as e:
        print(e)
        return False

# Sort the Array of the statistics of all scool
def sort_statistics(table, column_name='percentofAfricanAmericanStudents'):
    n = len(table)
    print(n)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            print('i ', i, 'j: ', j)
            print(type(table[j][1][1][column_name]))
            if table[j][1][1][column_name] > table[j + 1][1][1][column_name]:
                table[j], table[j + 1] = table[j + 1], table[j]
            print(table)

    return table


def main():
    directory = 'data/'
    i = 0
    statistics_ = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = json.load(file)

            # print(percentofAfricanAmericanStudents(filename[:-5], content, 2022))
            statistics_.append(list(percentofAfricanAmericanStudents(filename[:-5], content, [2023, 2022, 2021, 2020]).items()))
            # print(stat)

    sorted = sort_statistics(statistics_)

    for row in sorted:
        print(row)

    #
    # state_abr_list = \
    #     ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY'
    #         , 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND'
    #         , 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', ]


    # for state in state_abr_list:
    #     data = getData(state)
    #     statistics_.append(list(percentofAfricanAmericanStudents(state, data, [2023, 2022, 2021, 2020]).items()))
    #
    # print(statistics_)

    return


if __name__ == '__main__':
    main()
