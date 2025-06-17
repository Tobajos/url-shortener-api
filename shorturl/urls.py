from django.urls import path
from .views import ShortenURLView, ExpandURLView

urlpatterns = [
    path('shorten/', ShortenURLView.as_view(), name='shorten'),
    path('expand/<str:short_code>/', ExpandURLView.as_view(), name='expand'),
]
