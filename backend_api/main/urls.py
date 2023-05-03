from django.urls import path
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('roles2', views.RolesViewSet)
router.register('ethnicity', views.EthnicityViewSet)

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('project/<int:pk>', views.ProjectDetail.as_view()),
    path('backlogitems/', views.BacklogList.as_view()),
    path('backlogitem/<int:pk>', views.BacklogItemDetail.as_view()),
    path('workevents/', views.WorkEventList.as_view()),
    path('workevent/<int:pk>', views.WorkEventDetail.as_view()),
    path('organizations/', views.OrganizationList.as_view()),
    path('organization/<int:pk>', views.OrganizationDetail.as_view()),
    path('stakeholders/', views.StakeholderList.as_view()),
    path('stakeholder/<int:pk>', views.StakeholderDetail.as_view()),
    path('assignments/', views.AssignmentList.as_view()),
    path('assignment/<int:pk>', views.AssignmentDetail.as_view()),
    path('lifecycles/', views.LifeCycleList.as_view()),
    path('lifecycle/<int:pk>', views.LifeCycleDetail.as_view()),
    path('statuslist/', views.StatusList.as_view()),
    path('status/<int:pk>', views.StatusDetail.as_view()),
    path('genders/', views.GenderList.as_view()),
    path('gender/<int:pk>', views.GenderDetail.as_view()),
    
    
]

urlpatterns += router.urls