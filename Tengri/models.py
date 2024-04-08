from django.db import models


# Create your models here.
class Article(models.Model):
    project_id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=200, null=False, blank=False, default="No title")
    authors = models.CharField(max_length=200, blank=True, null=True)
    main_text = models.TextField(blank=True, null=True)
    main_link = models.CharField(max_length=200)
    project_date = models.DateTimeField(blank=True, null=True)
    project_logo = models.CharField(max_length=200, blank=True, null=True)
    project_tags = models.TextField(blank=True, null=True)

