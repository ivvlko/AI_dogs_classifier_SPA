from rest_framework import serializers
from api.models import ImageClassification


class ImageClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageClassification
        fields = '__all__'
