# evreka_assessment

Django 3.1.1

Django rest framework 3.11.1

Steps to run:

take git clone

run `pip install -r requirements.txt` to install the required libraries.

run `./manage.py runserver` to run the server.

To get the the list of last points per vehicle that have sent navigation data in the last 48 hours use the following cURL:

`curl --location --request GET 'http://localhost:8000/evreka/navigation_records/' \
--header 'Content-Type: application/json' \
--data-raw ''`
