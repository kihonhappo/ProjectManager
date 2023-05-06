from rest_framework import serializers
from . import models

# The serializer class takes the model object and will map or serialize the data from the view into a JSON object.
# The Meta fields property is where you add or remove data fields from the serialized JSON object
# The self def allows the serializer to populate any foreign key linked records. 
# I.E. The Owner in the Project model is linked to the Stakeholder table. The depth function will grab the associated object data and serialize 
# it with the Project data instead of just sending the StakeholderID. You can serialize as far in depth as you like but the deeper you go the 
# more processing you use.
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = ['ProjectID','Title','Start_Date','Owner']
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
        fields = ['StakeholderID','First_Name','Last_Name','Title','Gender','Ethnicity','Organization']
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