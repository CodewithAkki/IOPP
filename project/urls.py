from django.urls import path
from .views import CreateMailestone,CreateListApprove,CreateListDomain,CreateListGoal,CreateListGroup,CreateListRepository,CreateProject
from .views import UpdateDeleteRetriveMailestone,UpdateDeleteRetriveApproval,UpdateDeleteRetriveDomain,UpdateDeleteRetriveGoal,UpdateDeleteRetriveGroup,UpdateDeleteRetriveProject,UpdateDeleteRetriveRepository
urlpatterns = [
    
    path('CreateListApprove/',CreateListApprove.as_view()),
    path('CreateListDomain/',CreateListDomain.as_view()),
    path('CreateListGoal/',CreateListGoal.as_view()),
    path('CreateListGroup/',CreateListGroup.as_view()),
    path('CreateListRepository/',CreateListRepository.as_view()),
    path('CreateProject/',CreateProject.as_view()),
    path('CreateMailstone/',CreateMailestone.as_view()),

    path('UpdateDeleteRetriveApproval/<uuid:pk>',UpdateDeleteRetriveApproval.as_view()),
    path('UpdateDeleteRetriveGoal/<uuid:pk>',UpdateDeleteRetriveGoal.as_view()),
    path('UpdateDeleteRetriveDomain/<uuid:pk>',UpdateDeleteRetriveDomain.as_view()),
    path('UpdateDeleteRetriveGroup/<uuid:pk>',UpdateDeleteRetriveGroup.as_view()),
    path('UpdateDeleteRetriveMailstone/<uuid:pk>',UpdateDeleteRetriveMailestone.as_view()),
    path('UpdateDeleteRetriveProject/<uuid:pk>',UpdateDeleteRetriveProject.as_view()),
    
]
