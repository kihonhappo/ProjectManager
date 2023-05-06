from rest_framework import serializers
from . import models

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = ['ProjectID','Title','Start_Date']
    def __init__(self, *args, **kwargs):
        
        super(ProjectSerializer, self).__init__(self, *args, **kwargs) 
        self.Meta.depth = 1

class BackLogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BacklogItems
        fields = ['BacklogItemID','Title','Start_Date']
    def __init__(self, *args, **kwargs):
        super(BackLogItemSerializer, self).__init__(self, *args, **kwargs) 
        self.Meta.depth = 1
class WorkEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkEvents
        fields = ['WorkEventID','Title','Work_Date']
    def __init__(self, *args, **kwargs):
        super(WorkEventSerializer, self).__init__(self, *args, **kwargs) 
        self.Meta.depth = 1
class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stakeholders
        fields = ['StakeholderID','First_Name','Last_Name','Gender','Ethnicity','Organization']
    def __init__(self, *args, **kwargs):
        super(StakeholderSerializer, self).__init__(self, *args, **kwargs) 
        self.Meta.depth = 1 
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organizations
        fields = ['OrganizationID','Title','Description']
    def __init__(self, *args, **kwargs):
        super(OrganizationSerializer, self).__init__(self, *args, **kwargs) 
        self.Meta.depth = 1

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Assignments
        fields = ['AssignmentID','Project','Stakeholder'] 
    def __init__(self, *args, **kwargs):
        super(AssignmentSerializer, self).__init__(self, *args, **kwargs) 
        self.Meta.depth = 1

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Types
        fields = ['TypeI','Title','Description']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = ['StatusID','Title','Description']
class LifeCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LifeCycle
        fields = ['LifeCycleID','Title','Description']

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gender
        fields = ['GenderID','Title','Description']
class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ethnicity
        fields = ['EthnicityID','Title','Description']
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Roles
        fields = ['RoleID','Title','Description']