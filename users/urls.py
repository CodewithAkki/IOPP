from django.urls import path
from .views import CreateUser,searchguid,userDetails ,RoleInfo, RoleDetails, deleteAll,UpdateDeleteRetrive , seachThroughRole
urlpatterns = [
    path('',CreateUser.as_view()),
    path('guid/<int:id>',searchguid.as_view()),
    path('<int:id>',UpdateDeleteRetrive.as_view()),
    path('update/<int:id>',userDetails.as_view()),
    path('<str:role>',seachThroughRole.as_view()),
    path('delusers/',deleteAll.as_view()),
    path('role/',RoleInfo.as_view()),
    path('role/<int:pk>',RoleDetails.as_view()),
]