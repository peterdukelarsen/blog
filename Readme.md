# Blog

## Getting Started Locally
1. Have python 3.6 installed
2. `python3 -m venv blogenv`
3. `source blogenv/bin/activate`
4. `pip install -r requirements.txt`
5. `export DEBUG=true`
6. `export SECRET_KEY=1`
7. `python manage.py migrate`
8. `python manage.py runserver`
