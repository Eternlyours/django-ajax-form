from django.urls import path

from .views import HomeView, PostCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', PostCreateView.as_view(), name='add'),
]
