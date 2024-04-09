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
