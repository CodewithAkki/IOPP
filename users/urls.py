from django.urls import path
from .views import CreateUser , UpdateDeleteRetrive
urlpatterns = [
    path('',CreateUser.as_view()),
    path('<int:pk>',UpdateDeleteRetrive.as_view()),
]