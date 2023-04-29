from django.urls import path
from .views import CreateMailestone,CreateListApprove,CreateListDomain,CreateListGoal,CreateListGroup,CreateListRepository,CreateProject
from .views import AssignmentGuidsDetail,AssignmentGuidsUpdate,UpdateDeleteRetriveMailestone,SearchDeleteGroup,UpdateDeleteRetriveApproval,UpdateDeleteRetriveDomain,UpdateDeleteRetriveGoal,UpdateDeleteRetriveGroup,UpdateDeleteRetriveProject,UpdateDeleteRetriveRepository
urlpatterns = [
    
    path('Approve/',CreateListApprove.as_view()),
    path('Domain/',CreateListDomain.as_view()),
    path('Goal/',CreateListGoal.as_view()),
    path('Group/',CreateListGroup.as_view()),
    path('Repository/',CreateListRepository.as_view()),
    path('',CreateProject.as_view()),
    path('Mailstone/',CreateMailestone.as_view()),
    path('Assignment',AssignmentGuidsDetail.as_view()),
    path('Assignment/<int:pk>',AssignmentGuidsUpdate.as_view()),

    path('Approval/<uuid:pk>',UpdateDeleteRetriveApproval.as_view()),
    path('group/<str:name>',SearchDeleteGroup.as_view()),
    path('Goal/<uuid:pk>',UpdateDeleteRetriveGoal.as_view()),
    path('Domain/<uuid:pk>',UpdateDeleteRetriveDomain.as_view()),
    path('Group/<int:pk>',UpdateDeleteRetriveGroup.as_view()),
    path('Mailstone/<uuid:pk>',UpdateDeleteRetriveMailestone.as_view()),
    path('<uuid:pk>/',UpdateDeleteRetriveProject.as_view()),
    
]
