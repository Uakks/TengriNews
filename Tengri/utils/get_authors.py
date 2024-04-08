from ..models import Article


class ArticleAuthors:
    def get_authors(self, pr_id):
        article = Article.objects.get(project_id=pr_id)
        auts = article.authors
        auths = auts.split("'")
        authors_list = []
        for author in auths:
            print(len(author))
            if len(author) > 2:
                authors_list.append(author)
        return authors_list
