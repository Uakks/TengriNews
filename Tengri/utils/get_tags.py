import os
import json
from ..models import Article


class ArticleParser:
    def get_tags(self):

        cwd = os.getcwd()
        abspath = os.path.abspath(os.path.join(cwd))

        all_tags = set()
        with open(f'{abspath}/projects_data.json') as json_file:
            data = json.load(json_file)

            for article in data:
                for tag in article['project_tags']:
                    all_tags.add(tag)
        sorted_tags = sorted(all_tags, key=str.lower)
        return sorted_tags
