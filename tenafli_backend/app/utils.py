import requests
import datetime


# Compute the Number(Value) associated with a percentage given the totalNumber
def computeNumberFromPercentage(totalNumber, percentage):
    return round(percentage * (totalNumber / 100))


# Compute the Percentage of Number given the totalNumber
def computePercentageFromNumber(totalNumber, number):
    try:
        return (number / totalNumber) * 100
    except:
        return 0

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

    if data:
        totalStudent = 0
        totalAfricanAmericanStudent = 0

        for school in data['schoolList']:

            try:
                schoolYearlyDetails = school['schoolYearlyDetails']

                for schoolYearlyDetail in schoolYearlyDetails:

                    if is_list:
                        if schoolYearlyDetail['year'] in year :
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


# Sort the Array of the statistics of all school
def sort_statistics(table, top=5,column_name='percentofAfricanAmericanStudents'):
    n = len(table)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if table[j][1][1][column_name] > table[j + 1][1][1][column_name]:
                table[j], table[j + 1] = table[j + 1], table[j]
    table = table[::-1]
    return table[:top]

