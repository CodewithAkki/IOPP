from django.urls import path
from .views import CreateMailestone,CreateListApprove,CreateListDomain,CreateListGoal,CreateListGroup,CreateListRepository,CreateProject
from .views import UpdateDeleteRetriveMailestone,UpdateDeleteRetriveApproval,UpdateDeleteRetriveDomain,UpdateDeleteRetriveGoal,UpdateDeleteRetriveGroup,UpdateDeleteRetriveProject,UpdateDeleteRetriveRepository
urlpatterns = [
    
    path('Approve/',CreateListApprove.as_view()),
    path('Domain/',CreateListDomain.as_view()),
    path('Goal/',CreateListGoal.as_view()),
    path('Group/',CreateListGroup.as_view()),
    path('Repository/',CreateListRepository.as_view()),
    path('',CreateProject.as_view()),
    path('Mailstone/',CreateMailestone.as_view()),

    path('Approval/<uuid:pk>',UpdateDeleteRetriveApproval.as_view()),
    path('Goal/<uuid:pk>',UpdateDeleteRetriveGoal.as_view()),
    path('Domain/<uuid:pk>',UpdateDeleteRetriveDomain.as_view()),
    path('Group/<uuid:pk>',UpdateDeleteRetriveGroup.as_view()),
    path('Mailstone/<uuid:pk>',UpdateDeleteRetriveMailestone.as_view()),
    path('<uuid:pk>/',UpdateDeleteRetriveProject.as_view()),
    
]
