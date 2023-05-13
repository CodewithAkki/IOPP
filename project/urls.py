from django.urls import path
from .views import CreateMailestone,CreateListApprove,CreateListDomain,CreateListGoal,CreateListGroup,CreateProject
from .views import searchByproject,guidtohod,projectguid,AssignmentGuidsDetail,AssignedProjects,AssignmentGuidsUpdate,UpdateDeleteRetriveMailestone,UpdateDeleteRetriveApproval,UpdateDeleteRetriveDomain,UpdateDeleteRetriveGoal,UpdateDeleteRetriveGroup,UpdateDeleteRetriveProject
from .views import hodtodean,deantoAicte
urlpatterns = [
    
    path('Approve/',CreateListApprove.as_view()),
    path('Domain/',CreateListDomain.as_view()),
    path('Goal/',CreateListGoal.as_view()),
    path('Group',CreateListGroup.as_view()),
   
    path('',CreateProject.as_view()),
    path('Mailstone/',CreateMailestone.as_view()),
    path('Assignment',AssignmentGuidsDetail.as_view()),
    path('Assignment/<uuid:id>',AssignmentGuidsUpdate.as_view()),
    path('Approve/<uuid:collect_projects>',searchByproject.as_view()),
    path('Approval/<uuid:pk>',UpdateDeleteRetriveApproval.as_view()),
    
    path('Goal/<uuid:pk>',UpdateDeleteRetriveGoal.as_view()),
    path('Domain/<uuid:pk>',UpdateDeleteRetriveDomain.as_view()),
    path('Group/<uuid:project>',UpdateDeleteRetriveGroup.as_view()),
    path('Mailstone/<uuid:id>',UpdateDeleteRetriveMailestone.as_view()),
    path('<uuid:id>/',UpdateDeleteRetriveProject.as_view()),
    path('Assigned/<str:role>/<int:userid>',AssignedProjects.as_view()),
    path('assignedguid/<int:guid>',projectguid.as_view()),

    path('guidtohod/<str:college>/<int:projectid>',guidtohod.as_view()),
    path('hodtodean/<str:college>/<int:projectid>',hodtodean.as_view()),
    path('deantoaicte/<str:college>/<int:projectid>',deantoAicte.as_view()),
]
