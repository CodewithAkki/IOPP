from events.views import Event_details,Event_info
from rest_framework.urls import path

urlpatterns = [

    path('',Event_info.as_view()),
    path('<int:pk>',Event_details.as_view()),

]
