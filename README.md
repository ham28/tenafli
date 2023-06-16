# tenafli
code for the test at Tenafli

# Creation date:
in june 10 2023

# Installation

<p>Clone the repository:</p> 

`git clone https://github.com/ham28/tenafli.git`

<p> Go inside the tenafli directory </p>

`cd tenafli`

<p>Open a terminal prompt to create a new Virtual Environment.</p> 
<p>Inside the terminal prompt execute:</p>

`python3 -m venv env`

<p>then activate this new environment</p>

`source env/bin/activate`

<p>Install dependencies:</p>
`pip install -r requirement.txt`

# For the CLI
 `python Backend/DataManagement.py`

# For the API 
### Running Project
`python tenafli_backend/manage.py makemigrations`

`python tenafli_backend/manage.py migrate`

`python tenafli_backend/manage.py runserver`

Go to the indicated URL http://127.0.0.1:8000

Or directly through the browser, by going to the URL http://127.0.0.1:8000

### Params in the browser:

<p>you can add some params in the browser as below</p>

http://127.0.0.1:8000/?top=10&column_name=totalofAfricanAmericanStudents&year=2020,2019

- top: get the top number you want to have (default value = 5 )
- column_name: can be switch between 'totalStudent', 'totalofAfricanAmericanStudents',percentofAfricanAmericanStudents (default value = 'percentofAfricanAmericanStudents') 
- year: can be a single year(as: 2020), can be list of year(2020,2023,2021). The default value is the current year