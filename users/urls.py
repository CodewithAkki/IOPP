from django.urls import path
from .views import CreateUser ,RoleInfo, RoleDetails, deleteAll,UpdateDeleteRetrive , seachThroughRole
urlpatterns = [
    path('',CreateUser.as_view()),
    path('<int:pk>',UpdateDeleteRetrive.as_view()),
    path('<str:role>',seachThroughRole.as_view()),
    path('delusers/',deleteAll.as_view()),
    path('role/',RoleInfo.as_view()),
    path('role/<str:name>',RoleDetails.as_view()),
]