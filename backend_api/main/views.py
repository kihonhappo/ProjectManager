from rest_framework import generics,permissions,pagination,viewsets
from . import serializers
from . import models
from rest_framework.response import Response

# A view function, or view, is a Python function that takes a web request and returns a web response. This response can be the HTML 
# contents of a web page, or a redirect, or a 404 error, or an XML document, an image or anything.

# This function recieves the web request for a list of projects or other requested api and then queries the Postgres DB and then uses the 
# requested objects serializer to convert the returned data into a JSON transpert object and send it back to the React app.
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