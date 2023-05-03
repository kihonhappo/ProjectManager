from rest_framework import serializers
from . import models

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = ['ProjectID','Title','Start_Date','Owner']
    def __init__(self, *args, **kwargs):
        super(ProjectSerializer, self).__init__(self, *args, **kwargs) 
        request = self.context.get('request')
        self.Meta.depth = 2

class BackLogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BacklogItems
        fields = ['BacklogItemID','Title','Start_Date']
    def __init__(self, *args, **kwargs):
        super(BackLogItemSerializer, self).__init__(self, *args, **kwargs) 
        request = self.context.get('request')
        self.Meta.depth = 2


class WorkEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkEvents
        fields = ['WorkEventID','Title','Work_Date']
    def __init__(self, *args, **kwargs):
        super(WorkEventSerializer, self).__init__(self, *args, **kwargs) 
        request = self.context.get('request')
        self.Meta.depth = 2


class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stakeholders
        fields = ['StakeholderID','First_Name','Last_Name','Gender','Ethnicity','Organization']
    def __init__(self, *args, **kwargs):
        super(StakeholderSerializer, self).__init__(self, *args, **kwargs) 
        request = self.context.get('request')
        self.Meta.depth = 1 

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organizations
        fields = ['OrganizationID','Title','Description']
    def __init__(self, *args, **kwargs):
        super(OrganizationSerializer, self).__init__(self, *args, **kwargs) 
        request = self.context.get('request')
        self.Meta.depth = 1

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Assignments
        fields = ['AssignmentID','Project','Stakeholder'] 
    def __init__(self, *args, **kwargs):
        super(AssignmentSerializer, self).__init__(self, *args, **kwargs) 
        request = self.context.get('request')
        self.Meta.depth = 1

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Types
        fields = ['TypeI','Title','Description']
  #  def __init__(self, *args, **kwargs):
   #     super(TypeListSerializer, self).__init__(self, *args, **kwargs) 

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = ['StatusID','Title','Description']
   # def __init__(self, *args, **kwargs):
   #    super(StatusListSerializer, self).__init__(self, *args, **kwargs) 

class LifeCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LifeCycle
        fields = ['LifeCycleID','Title','Description']
   # def __init__(self, *args, **kwargs):
    ##    super(LifeCycleListSerializer, self).__init__(self, *args, **kwargs) 


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gender
        fields = ['GenderID','Title','Description']
  # def __init__(self, *args, **kwargs):
    #    super(GenderListSerializer, self).__init__(self, *args, **kwargs) 


class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ethnicity
        fields = ['EthnicityID','Title','Description']
   # def __init__(self, *args, **kwargs):
    #    super(EthnicityListSerializer, self).__init__(self, *args, **kwargs) 


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Roles
        fields = ['RoleID','Title','Description']
   # def __init__(self, *args, **kwargs):
    #  super(Role2Serializer, self).__init__(self, *args, **kwargs) 
     #  self.Meta.depth """