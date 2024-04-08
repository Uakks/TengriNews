import json
from ..models import Article

class ArticleParser:
    def __init__(self):
        pass

    def get_tags():
        all_tags = set()
        with open('../TengriNews/projects_data.json') as json_file:
            data = json.load(json_file)

            for article in data:
                for tag in article['project_tags']:
                    all_tags.add(tag)

        return all_tags
