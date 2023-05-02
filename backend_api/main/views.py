from rest_framework import generics
from . import serializers
from . import models

# Create your views here.

class ProjectList(generics.ListCreateAPIView):
    queryset = models.Projects.objects.all()
    serializer_class = serializers.ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Projects.objects.all()
    serializer_class = serializers.ProjectDetailSerializer

class BacklogList(generics.ListAPIView):
    queryset = models.BacklogItems.objects.all()
    serializer_class = serializers.BackLogItemSerializer

class WorkEventList(generics.ListAPIView):
    queryset = models.WorkEvents.objects.all()
    serializer_class = serializers.WorkEventSerializer

class StakeholderList(generics.ListAPIView):
    queryset = models.Stakeholders.objects.all()
    serializer_class = serializers.StakeholderSerializer

class AssignmentList(generics.ListAPIView):
    queryset = models.Assignments.objects.all()
    serializer_class = serializers.AssignmentSerializer

class OrganizationList(generics.ListAPIView):
    queryset = models.Organizations.objects.all()
    serializer_class = serializers.OrganizationSerializer

class TypeList(generics.ListAPIView):
    queryset = models.Types.objects.all()
    serializer_class = serializers.TypeSerializer

class StatusList(generics.ListAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer

class LifeCycleList(generics.ListAPIView):
    queryset = models.LifeCycle.objects.all()
    serializer_class = serializers.LifeCycleSerializer

class GenderList(generics.ListAPIView):
    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderSerializer

class EthnicityList(generics.ListAPIView):
    queryset = models.Ethnicity.objects.all()
    serializer_class = serializers.EthnicitySerializer

class RoleList(generics.ListAPIView):
    queryset = models.Roles.objects.all()
    serializer_class = serializers.RoleSerializer