from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from api.forms import ImageClassificationForm
from api.models import ImageClassification
from api.serializers import ImageClassificationSerializer

from api.ai_workshop import give_top_three_candidates, model, named_labels, read_tensor_from_image_url
import requests


class ApiGetPost(APIView):

    def get(self, request, format=None):
        info = ImageClassification.objects.all()
        serializer = ImageClassificationSerializer(info, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ImageClassificationSerializer(data=request.data)
        if serializer.is_valid():
            image_url = serializer.validated_data['url']
            image = read_tensor_from_image_url(
                image_url
            )
            scores = give_top_three_candidates(image, model, named_labels)
            serializer.validated_data['prediction1'] = scores[0]
            serializer.validated_data['prediction2'] = scores[1]
            serializer.validated_data['prediction3'] = scores[2]
            serializer.save()
            return Response(serializer.data)
        return Response('Something Went Wrong. Try with another URL.')


def landing_page(req):
    form = ImageClassificationForm()
    context = {
        'form': form,
    }
    return render(req, 'spa_page.html', context)


