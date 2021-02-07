from django.urls import path
from api.views import landing_page, ApiGetPost

urlpatterns = [
    path('api/', ApiGetPost.as_view(), name='api-main'),
    path('', landing_page, name='landing_page'),
]