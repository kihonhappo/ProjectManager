from rest_framework import generics,permissions,pagination,viewsets
from . import serializers
from . import models

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Projects.objects.all()
    serializer_class = serializers.ProjectSerializer
class BacklogViewSet(viewsets.ModelViewSet):
    queryset = models.BacklogItems.objects.all()
    serializer_class = serializers.BackLogItemSerializer
class WorkEventViewSet(viewsets.ModelViewSet):
    queryset = models.WorkEvents.objects.all()
    serializer_class = serializers.WorkEventSerializer
class StakeholderViewSet(viewsets.ModelViewSet):
    queryset = models.Stakeholders.objects.all()
    serializer_class = serializers.StakeholderSerializer
    
class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = models.Assignments.objects.all()
    serializer_class = serializers.AssignmentSerializer
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = models.Organizations.objects.all()
    serializer_class = serializers.OrganizationSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = models.Types.objects.all()
    serializer_class = serializers.TypeSerializer

class LifeCycleViewSet(viewsets.ModelViewSet):
    queryset = models.LifeCycle.objects.all()
    serializer_class = serializers.LifeCycleSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer

class GenderViewSet(viewsets.ModelViewSet):
    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderSerializer
class EthnicityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EthnicitySerializer
    queryset = models.Ethnicity.objects.all()
class RolesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RoleSerializer
    queryset = models.Roles.objects.all()
    #def get_queryset(self):
    #  RoleID = self.kwargs['pk']