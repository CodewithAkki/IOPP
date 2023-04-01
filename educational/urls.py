from django.urls import path
from .views import CreatecCollege ,UpdateDeleteRetriveUniversity,CreatecUniversity, UpdateDeleteRetriveCollege
urlpatterns = [
  path('CreateListCollege/',CreatecCollege.as_view()),  
  path('UpdateDeleteRetriveCollege/<uuid:pk>',UpdateDeleteRetriveCollege.as_view()),  

  path('UpdateDeleteRetriveUniversity/<uuid:pk>',UpdateDeleteRetriveUniversity.as_view()),
  path('CreatecUniversity/',CreatecUniversity.as_view()),

]