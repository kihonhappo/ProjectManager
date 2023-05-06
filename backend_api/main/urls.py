from django.urls import path
from . import views 
from rest_framework import routers 

# This is where the client api requests are recieved and then send out according to the request

router = routers.DefaultRouter()
router.register('role', views.RolesViewSet)
router.register('ethnicity', views.EthnicityViewSet)
router.register('gender', views.GenderViewSet)
router.register('status', views.StatusViewSet)
router.register('project', views.ProjectViewSet)
router.register('backlog', views.BacklogViewSet)
router.register('workevent', views.WorkEventViewSet)
router.register('stakeholder', views.StakeholderViewSet)
router.register('organization', views.OrganizationViewSet)
router.register('assignment', views.AssignmentViewSet)
router.register('lifecycle', views.LifeCycleViewSet)

urlpatterns = router.urls