from django.urls import path
from .views import CreateUser , UpdateDeleteRetrive
urlpatterns = [
    path('ListCreateAPI/',CreateUser.as_view()),
    path('RetrieveUpdateDestroyAPI/<int:pk>',UpdateDeleteRetrive.as_view()),
]