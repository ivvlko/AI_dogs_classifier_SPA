from django.shortcuts import render
from rest_framework.response import Response, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.forms import ImageClassificationForm
from api.models import ImageClassification
from api.serializers import ImageClassificationSerializer
from api.ai_workshop import give_top_candidate, model, named_labels, read_tensor_from_image_url


class ListCreateView(ListCreateAPIView):
    queryset = ImageClassification.objects.all()
    serializer_class= ImageClassificationSerializer

    def post(self, request, *args, **kwargs):
        
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


class UpdateResultView(RetrieveUpdateDestroyAPIView):
    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = ImageClassification.objects.get(id=pk)
        serializer = ImageClassificationSerializer(obj, data=request.data)
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


