from django.db import models


class ImageClassification(models.Model):
    url = models.URLField(blank=True)
    prediction1 = models.CharField(max_length=200, blank=True)
    predicted_index = models.IntegerField(blank=True, default=-1)
    correct_prediction = models.IntegerField(blank=True, default=-1)
    confirmed_by_admin = models.BooleanField(blank=True, default=False)


