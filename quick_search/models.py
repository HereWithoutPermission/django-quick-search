from django.db import models

# Create your models here.
class SearchResult(models.Model):

    query = models.CharField(max_length=50)
    heading = models.CharField(max_length=200, default="No header available")
    url = models.CharField(max_length=200, default="#")
    text = models.CharField(max_length=2000, default="No body available")
    time_created = models.DateTimeField(auto_now_add=True)