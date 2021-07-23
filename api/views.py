from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from api.forms import ImageClassificationForm
from api.models import ImageClassification
from api.serializers import ImageClassificationSerializer
from api.ai_workshop import give_top_candidate, model, named_labels, read_tensor_from_image_url
from rest_framework.decorators import api_view


@api_view(['GET',  "POST"])
def api(request):
    if request.method == 'GET':
        info = ImageClassification.objects.all()
        serializer = ImageClassificationSerializer(info, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ImageClassificationSerializer(data=request.data)
        if serializer.is_valid():
            image_url = serializer.validated_data['url']
            image = read_tensor_from_image_url(
                image_url
            )
            scores = give_top_candidate(image, model, named_labels)
            serializer.validated_data['prediction1'] = scores[0]
            serializer.validated_data['predicted_index'] = scores[1]
            serializer.save()
            return Response(serializer.data)
        return Response('Something Went Wrong. Try with another URL.')


@api_view(['GET', "PUT"])
def api_details(request, pk):
    try:
        snippet = ImageClassification.objects.get(id=pk)
    except ImageClassification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ImageClassificationSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        snippet = ImageClassification.objects.get(id=pk)
        serializer = ImageClassificationSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def landing_page(req):
    form = ImageClassificationForm()
    context = {
        'form': form,
    }
    return render(req, 'spa_page.html', context)


