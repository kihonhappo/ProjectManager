from rest_framework import serializers
from . import models

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = ['ProjectID','Title','Start_Date']
    def __init__(self, *args, **kwargs):
        super(ProjectSerializer, self).__init__(self, *args, **kwargs) 


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = ['ProjectID','Title','Start_Date']
    def __init__(self, *args, **kwargs):
        super(ProjectDetailSerializer, self).__init__(self, *args, **kwargs) 
        self.Meta.depth = 1

class BackLogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BacklogItems
        fields = ['Title','Start_Date']

class WorkEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkEvents
        fields = ['Title','Work_Date']

class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stakeholders
        fields = ['First_Name','Last_Name']

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organizations
        fields = ['Title','Description']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Assignments
        fields = ['Project','Stakeholder'] 

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Types
        fields = ['Title','Description']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = ['Title','Description']

class LifeCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LifeCycle
        fields = ['Title','Description']

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gender
        fields = ['Title','Description']

class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ethnicity
        fields = ['Title','Description']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Roles
        fields = ['RoleID','Title','Description']