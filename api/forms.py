from django import forms

from api.models import ImageClassification


class ImageClassificationForm(forms.ModelForm):
    class Meta:
        model = ImageClassification
        fields = ['url']
