import json
import os

from django.core.management.base import BaseCommand
from Tengri.models import Article


class Command(BaseCommand):
    help = 'Import articles from json file into database'

    def handle(self, *args, **kwargs):
        cwd = os.getcwd()
        abspath = os.path.abspath(os.path.join(cwd))
        with open(f'{abspath}/projects_data.json', 'r', encoding='utf8') as file:
            data = json.load(file)

            for article in data:
                Article.objects.create(
                    project_id=article['project_id'],
                    title=article['title'],
                    authors=article['authors'],
                    main_text=article['main_text'],
                    main_link = article['main_link'],
                    project_date = article['project_date'],
                    project_logo = article['project_logo'],
                    project_tags = article['project_tags']
                )
        self.stdout.write(self.style.SUCCESS('Done'))