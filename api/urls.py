from django.urls import path
from api.views import landing_page, ListCreateView, UpdateResultView

urlpatterns = [
    path('api/', ListCreateView.as_view(), name='api-main'),
    path('api_details/<int:pk>/', UpdateResultView.as_view()),
    path('', landing_page, name='landing_page'),
]