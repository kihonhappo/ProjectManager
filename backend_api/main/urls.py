from django.urls import path
from . import views 
urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('project/<int:pk>', views.ProjectDetail.as_view()),
    path('backlogitems/', views.BacklogList.as_view()),
    path('workevents/', views.WorkEventList.as_view()),
    path('organizations/', views.OrganizationList.as_view()),
    path('stakeholders/', views.StakeholderList.as_view()),
    path('assignments/', views.AssignmentList.as_view()),
    path('lifecycles/', views.LifeCycleList.as_view()),
    path('status/', views.StatusList.as_view()),
    path('roles/', views.RoleList.as_view()),
    path('genders/', views.GenderList.as_view()),
    path('ethnicity/', views.EthnicityList.as_view()),
]
