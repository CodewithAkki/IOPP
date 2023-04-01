from django.urls import path
from .views import CreateUser , UpdateDeleteRetrive
urlpatterns = [
    path('user/',CreateUser.as_view()),
    path('user/<int:pk>',UpdateDeleteRetrive.as_view()),
]