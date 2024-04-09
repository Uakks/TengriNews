import json
import os

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
import datetime
import lxml

all_tags = set()
projects_data_list = []
months = {
    "января": 1,
    "февраля": 2,
    "марта": 3,
    "апреля": 4,
    "мая": 5,
    "июня": 6,
    "июля": 7,
    "августа": 8,
    "сентября": 9,
    "октября": 10,
    "ноября": 11,
    "декабря": 12,
}


def converter_to_datetime(lst):
    time = str(datetime.datetime.strptime(lst[3], "%H:%M")).split(" ")[-1]
    st = lst[2] + "-" + str(months[lst[1]]) + "-" + lst[0]
    proj_date = datetime.datetime.strptime(st + " " + time, "%Y-%m-%d %H:%M:%S")
    return proj_date


class Command(BaseCommand):
    def handle(self, *args, **options):
        pass

    def get_data(self, url):
        headers = {
            "user-agent": "Mozilla / 5.0(Macintosh; Intel Mac OS X 10_15_7) AppleWebKit / 537.36(KHTML, like Gecko) Chrome/123.0.0.0 Safari / 537.36"
        }

        cwd = os.getcwd()
        abspath = os.path.abspath(os.path.join(cwd))
        os.mkdir(f"{abspath}/data")

        iters = 11

        for i in range(1, iters):
            req = requests.get(url + f"page/{i}", headers)
            print(url + f"page/{i}")

            folder_name = f"{abspath}/data/data_{i}"

            if not os.path.exists(folder_name):
                os.mkdir(folder_name)

            with open(f'{folder_name}/source_{i}.html', 'w') as file:
                file.write(req.text)

            with open(f'{folder_name}/source_{i}.html') as file:
                src = file.read()

            soup = BeautifulSoup(src, "lxml")
            req = soup.find_all("div", class_="content_main_item")
            project_urls = []
            for item in req:
                link = item.find("a").get("href")
                if not link.startswith("https:"):
                    link = "https://tengrinews.kz" + link
                project_urls.append(link)

            for u in project_urls:
                req = requests.get(u, headers)
                name = u.split("/")[-2]

                with open(f"{folder_name}/{name}.html", "w") as file:
                    file.write(req.text)

                with open(f"{folder_name}/{name}.html") as file:
                    src = file.read()

                soup = BeautifulSoup(src, "lxml")
                project_data = soup.find("section", class_="first")
                # print(project_data)

                # All needed information about each post
                try:
                    proj_id = u.split("-")[-1]
                    project_id = proj_id.split("/")[0]
                except Exception:
                    continue

                try:
                    date = project_data.find("div", class_="date-time").text.split(" ")
                    if len(date) == 2:
                        if date[0] == "Вчера":
                            exact_time = datetime.datetime.strptime(date[1], "%H:%M")
                            exact_date = datetime.date.today() - datetime.timedelta(days=1)
                            project_date = datetime.datetime.strptime(
                                str(exact_date) + " " + str(exact_time).split(" ")[-1],
                                "%Y-%m-%d %H:%M:%S")
                        elif date[0] == "Сегодня":
                            exact_time = datetime.datetime.strptime(date[1], "%H:%M")
                            exact_date = datetime.date.today()
                            project_date = datetime.datetime.strptime(
                                str(exact_date) + " " + str(exact_time).split(" ")[-1],
                                "%Y-%m-%d %H:%M:%S")
                    if len(date) == 4:
                        project_date = converter_to_datetime(date)
                    # print(project_date)
                except Exception:
                    project_date = datetime.datetime.today()

                try:
                    project_logo = "https://tengrinews.kz" + project_data.find("div", class_="content_main_thumb").find(
                        "img").get("src")
                    # print(project_logo)
                except Exception:
                    project_logo = "No logo found"

                try:
                    project_authors = []
                    authors = project_data.find_all("span", class_="content_main_meta_author_item_name")
                    for author in authors:
                        project_author = author.find("a")
                        project_authors.append(project_author.text)
                    # print(project_authors)
                except Exception:
                    project_authors = []

                try:
                    project_title = project_data.find("h1", class_="head-single").text
                    # print(project_title)
                except Exception:
                    project_title = "News Title"

                # main text
                try:
                    project_main_text = project_data.find("div", class_="content_main_text").text
                    # print(project_main_text)
                except Exception:
                    project_main_text = "Article was not found"

                try:
                    project_main_link = url + u.split("/")[-2]
                    # print(project_main_link)
                except Exception:
                    project_main_link = ""

                try:
                    project_tags = []
                    project_tag_spans = project_data.find("div", class_="content_main_text_tags").find_all("span")
                    for tag in project_tag_spans:
                        project_tags.append(tag.text)
                        all_tags.add(tag.text)
                    # print(project_tags)
                except Exception:
                    project_tags = []

                projects_data_list.append(
                    {
                        "project_id": project_id,
                        "title": project_title,
                        "authors": project_authors,
                        "main_text": project_main_text,
                        "main_link": project_main_link,
                        "project_date": str(project_date),
                        "project_logo": project_logo,
                        "project_tags": project_tags
                    }
                )
            iters -= 1
            print(iters)
        with open(f"{abspath}/projects_data.json", "a", encoding="utf-8") as file:
            json.dump(projects_data_list, file, ensure_ascii=False, indent=4)


Command().get_data("https://tengrinews.kz/article/")
