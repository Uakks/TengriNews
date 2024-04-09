Hello! This is clone website of TengriNews portal.<br>
To properly run it on your PC follow this instructions:

1. First of all, clone git repository to any folder on your PC using this command:
```
git clone https://github.com/Uakks/TengriNews.git
```
<br>

2. In terminal or Command Line prompt enter this lines of code to activate virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
<br>

3. Install required libraries and packages
```
pip install -r requirements.txt
pip install requests
```
<br>

4. Migrate all models to database
```
python manage.py migrate
```
<br>

5. Parse 10 pages of articles from TengriNews portal
```
python manage.py parsing
```
<br>
Wait until every page is parsed. At the end there may be an error, but check the existence of projects_data.json file in root directory. If file exists everything worked.<br>
<br>

6. Import all parsed information from json file to database
```
python manage.py import_json
```
<br>

7. Run server
```
python manage.py runserver
```
<br>

8. Use the localhost and enjoy the news
```
 http://127.0.0.1:8000/
```
