from rest_framework import serializers
from . import models

class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = ['ProjectID','Title','Start_Date']
    #def __init__(self, *args, **kwargs):
        #super(ProjectListSerializer, self).__init__(self, *args, **kwargs) 


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = ['ProjectID','Title','Start_Date']
    #def __init__(self, *args, **kwargs):
        #super(ProjectDetailSerializer, self).__init__(self, *args, **kwargs) 
       # self.Meta.depth = 1

class BackLogItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BacklogItems
        fields = ['BacklogItemID','Title','Start_Date']
   # def __init__(self, *args, **kwargs):
    #    super(BackLogItemListSerializer, self).__init__(self, *args, **kwargs) 

class BackLogItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BacklogItems
        fields = ['BacklogItemID','Title','Start_Date']
  #  def __init__(self, *args, **kwargs):
   #     super(BackLogItemDetailSerializer, self).__init__(self, *args, **kwargs) 
    #    self.Meta.depth = 1


class WorkEventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkEvents
        fields = ['WorkEventID','Title','Work_Date']
   # def __init__(self, *args, **kwargs):
   #     super(WorkEventListSerializer, self).__init__(self, *args, **kwargs) 

class WorkEventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkEvents
        fields = ['WorkEventID','Title','Work_Date']
   # def __init__(self, *args, **kwargs):
     #   super(WorkEventDetailSerializer, self).__init__(self, *args, **kwargs) 
   #     self.Meta.depth = 1

class StakeholderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stakeholders
        fields = ['StakeholderID','First_Name','Last_Name']
  #  def __init__(self, *args, **kwargs):
     #   super(StakeholderListSerializer, self).__init__(self, *args, **kwargs) 

class StakeholderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stakeholders
        fields = ['StakeholderID','First_Name','Last_Name']
   # def __init__(self, *args, **kwargs):
   #     super(StakeholderDetailSerializer, self).__init__(self, *args, **kwargs)
    #    self.Meta.depth = 1 

class OrganizationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organizations
        fields = ['OrganizationID','Title','Description']
  #  def __init__(self, *args, **kwargs):
     #   super(OrganizationListSerializer, self).__init__(self, *args, **kwargs) 

class OrganizationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organizations
        fields = ['OrganizationID','Title','Description']
   # def __init__(self, *args, **kwargs):
     #   super(OrganizationDetailSerializer, self).__init__(self, *args, **kwargs) 
     #   self.Meta.depth = 1 

class AssignmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Assignments
        fields = ['AssignmentID','Project','Stakeholder'] 
  #  def __init__(self, *args, **kwargs):
    #    super(AssignmentListSerializer, self).__init__(self, *args, **kwargs) 
class AssignmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Assignments
        fields = ['AssignmentID','Project','Stakeholder'] 
   # def __init__(self, *args, **kwargs):
    #    super(AssignmentDetailSerializer, self).__init__(self, *args, **kwargs) 
   #     self.Meta.depth = 1 
class TypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Types
        fields = ['TypeID','Title','Description']
  #  def __init__(self, *args, **kwargs):
   #     super(TypeListSerializer, self).__init__(self, *args, **kwargs) 

class TypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Types
        fields = ['TypeID','Title','Description']
   # def __init__(self, *args, **kwargs):
   #     super(TypeDetailSerializer, self).__init__(self, *args, **kwargs) 
    #    self.Meta.depth = 1 

class StatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = ['StatusID','Title','Description']
   # def __init__(self, *args, **kwargs):
   #    super(StatusListSerializer, self).__init__(self, *args, **kwargs) 

class StatusDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = ['StatusID','Title','Description']
  #  def __init__(self, *args, **kwargs):
    #    super(StatusDetailSerializer, self).__init__(self, *args, **kwargs) 
     #   self.Meta.depth = 1

class LifeCycleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LifeCycle
        fields = ['LifeCycleID','Title','Description']
   # def __init__(self, *args, **kwargs):
    ##    super(LifeCycleListSerializer, self).__init__(self, *args, **kwargs) 

class LifeCycleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LifeCycle
        fields = ['LifeCycleID','Title','Description']
   # def __init__(self, *args, **kwargs):
    #    super(LifeCycleDetailSerializer, self).__init__(self, *args, **kwargs) 
   #    self.Meta.depth = 1

class GenderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gender
        fields = ['GenderID','Title','Description']
  # def __init__(self, *args, **kwargs):
    #    super(GenderListSerializer, self).__init__(self, *args, **kwargs) 

class GenderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gender
        fields = ['GenderID','Title','Description']
   # def __init__(self, *args, **kwargs):
    #    super(GenderDetailSerializer, self).__init__(self, *args, **kwargs) 
     #   self.Meta.depth = 1

class EthnicityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ethnicity
        fields = ['EthnicityID','Title','Description']
   # def __init__(self, *args, **kwargs):
    #    super(EthnicityListSerializer, self).__init__(self, *args, **kwargs) 

class EthnicityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ethnicity
        fields = ['EthnicityID','Title','Description']
  # def __init__(self, *args, **kwargs):
    #     super(EthnicityDetailSerializer, self).__init__(self, *args, **kwargs) 
    #    self.Meta.depth = 1 

class Role2Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Roles
        fields = ['RoleID','Title','Description']
   # def __init__(self, *args, **kwargs):
    #  super(Role2Serializer, self).__init__(self, *args, **kwargs) 
     #  self.Meta.depth """