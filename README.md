Hello! This is clone website of TengriNews portal.<br>
To properly run it on your PC follow these instructions:

1. First of all, clone git repository to any folder on your PC using this command:
```
git clone https://github.com/Uakks/TengriNews.git
```
<br>

2. In terminal or Command Line prompt enter this lines of code to activate virtual environment:
```
python3 -m venv venv

source venv/bin/activate  # MacOS
venv\Scripts\activate  # Windows
```
<br>

3. Build and run docker container
```
docker-compose build
docker-compose up -d
docker-compose logs -f
```

4. Enjoy using TengriNewsClone

Also check online hosted version by this link: https://tengrinews.onrender.com/

Main processes of building this app:<br>
First steps - designing the index.html file and constructing proper space for main page and adding all needed 
views and urls. Also creating news.html file for each article and styling everything<br>

Web-scraping - Interesting way of parsing data to local db by getting info from articles section in TengriNews and storing valuable 
information like article title, date, images, authors, main text and link for original article in json file,
which then was exported to local db.<br>

Searching - user can type anything and app will find any occurrences in title of articles.<br>

Filtration - each article had tags, filtration works by choosing one of the needed tag and searching.<br>

Pagination - works smoothly on main page. Implemented by built-in functions.<br>

Sorting - user can sort articles by alphabet order or date of publishing on main page.<br>

Docker - to deploy web-app I wrapped it all in docker and hosted it on render.com. Went smooth enough.<br>

Ways to improve:
1. Use more articles from main page of TengriNews and sort them by category, as I only took articles section for parsing.
2. Add search function for tags
3. Add pagination for search and sorted pages
3. Style each post page's main text, as it is only written in one style.
4. Maybe even add functionality to add your own articles to main feed.