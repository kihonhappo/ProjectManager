from rest_framework import generics,permissions,pagination,viewsets
from . import serializers
from . import models

# Create your views here.

class ProjectList(generics.ListCreateAPIView):
    queryset = models.Projects.objects.all()
    serializer_class = serializers.ProjectListSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Projects.objects.all()
    serializer_class = serializers.ProjectDetailSerializer
    
class BacklogList(generics.ListCreateAPIView):
    queryset = models.BacklogItems.objects.all()
    serializer_class = serializers.BackLogItemListSerializer

class BacklogItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BacklogItems.objects.all()
    serializer_class = serializers.BackLogItemDetailSerializer

class WorkEventList(generics.ListCreateAPIView):
    queryset = models.WorkEvents.objects.all()
    serializer_class = serializers.WorkEventListSerializer

class WorkEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.WorkEvents.objects.all()
    serializer_class = serializers.WorkEventDetailSerializer

class StakeholderList(generics.ListCreateAPIView):
    queryset = models.Stakeholders.objects.all()
    serializer_class = serializers.StakeholderListSerializer

class StakeholderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Stakeholders.objects.all()
    serializer_class = serializers.StakeholderListSerializer
class AssignmentList(generics.ListCreateAPIView):
    queryset = models.Assignments.objects.all()
    serializer_class = serializers.AssignmentListSerializer

class AssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Assignments.objects.all()
    serializer_class = serializers.AssignmentDetailSerializer

class OrganizationList(generics.ListCreateAPIView):
    queryset = models.Organizations.objects.all()
    serializer_class = serializers.OrganizationListSerializer

class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Organizations.objects.all()
    serializer_class = serializers.OrganizationDetailSerializer

class TypeList(generics.ListCreateAPIView):
    queryset = models.Types.objects.all()
    serializer_class = serializers.TypeListSerializer

class TypeDetail(generics.RetrieveUpdateAPIView):
    queryset = models.Types.objects.all()
    serializer_class = serializers.TypeDetailSerializer

class StatusList(generics.ListCreateAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusListSerializer

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusDetailSerializer

class LifeCycleList(generics.ListCreateAPIView):
    queryset = models.LifeCycle.objects.all()
    serializer_class = serializers.LifeCycleListSerializer

class LifeCycleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.LifeCycle.objects.all()
    serializer_class = serializers.LifeCycleDetailSerializer

class GenderList(generics.ListCreateAPIView):
    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderListSerializer

class GenderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderDetailSerializer

class EthnicityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EthnicityListSerializer
    queryset = models.Ethnicity.objects.all()
    

class RolesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Role2Serializer
    queryset = models.Roles.objects.all()
    #def get_queryset(self):
    #  RoleID = self.kwargs['pk']