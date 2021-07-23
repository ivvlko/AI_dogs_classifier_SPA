from django.urls import path
from api.views import landing_page, api, api_details

urlpatterns = [
    path('api/', api, name='api-main'),
    path('api_details/<int:pk>/', api_details),
    path('', landing_page, name='landing_page'),
]