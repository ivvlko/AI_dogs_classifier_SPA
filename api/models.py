from django.db import models


class ImageClassification(models.Model):
    url = models.URLField()
    prediction1 = models.CharField(max_length=200, blank=True)
    prediction2 = models.CharField(max_length=200, blank=True)
    prediction3 = models.CharField(max_length=200, blank=True)
