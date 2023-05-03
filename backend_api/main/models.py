from django.db import models
from django.contrib.auth.models import User

# Project models
class Projects(models.Model):  
    ProjectID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)
    Start_Date = models.DateField(null=True)
    End_Date = models.DateField(null=True)
    LifeCycle = models.ForeignKey("LifeCycle", on_delete=models.SET_NULL, null=True)
    Status = models.ForeignKey("Status", null=True, on_delete=models.SET_NULL)
    Owner = models.ForeignKey("Stakeholders", null=True, on_delete=models.SET_NULL)
    Note = models.TextField(null=True)

    def __str__(self):
        return self.Title
      
class BacklogItems(models.Model):
    BacklogItemID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Project = models.ForeignKey("Projects", null=True, on_delete=models.SET_NULL)
    Description = models.TextField(null=True)
    Projected_Hours = models.DecimalField(null=True, decimal_places=2, max_digits=6)
    Actual_Hours = models.DecimalField(null=True, decimal_places=2, max_digits=6)
    Start_Date = models.DateField(null=True)
    End_Date = models.DateField(null=True)
    Assigned_To = models.ForeignKey("Stakeholders", null=True, on_delete=models.SET_NULL)
    Plan = models.TextField(null=True)
    Note = models.TextField(null=True)
    Status = models.ForeignKey("Status", null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.Title
     
class WorkEvents(models.Model):
    WorkEventID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Project = models.ForeignKey("Projects", null=True, on_delete=models.SET_NULL)
    Backlog_Item = models.ForeignKey("BacklogItems", null=True, on_delete=models.SET_NULL)
    Owner = models.ForeignKey("Stakeholders", null=True, on_delete=models.SET_NULL)
    Work_Date = models.DateField(null=True)
    Start_Time = models.TimeField(null=True)
    End_Time = models.TimeField(null=True)
    Duration = models.DurationField(null=True)
    Work = models.TextField(null=True)
    Next_Steps = models.TextField(null=True)
    Note = models.TextField(null=True)
    def __str__(self):
        return self.Title
   
class Stakeholders(models.Model):
    StakeholderID = models.AutoField(primary_key=True, editable=False)
    First_Name = models.CharField(max_length=50, null=True)
    Last_Name = models.CharField(max_length=50, null=True)
    Organization = models.ForeignKey("Organizations", null=True, on_delete=models.SET_NULL)
    Title = models.CharField(max_length=50, null=True)
    Email = models.EmailField(null=True)
    Phone = models.CharField(max_length=50,null=True)
    Gender = models.ForeignKey("Gender", null=True, on_delete=models.SET_NULL)
    Ethnicity = models.ForeignKey("Ethnicity", null=True, on_delete=models.SET_NULL)
    User = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    Note = models.TextField(null=True)
    def __str__(self):
        return self.First_Name + ' ' + self.Last_Name
    
class Assignments(models.Model):
    AssignmentID = models.AutoField(primary_key=True, editable=False)
    Project = models.ForeignKey("Projects", null=True, on_delete=models.SET_NULL)
    Stakeholder = models.ForeignKey("Stakeholders", null=True, on_delete=models.SET_NULL)
    Role = models.ForeignKey("Roles", null=True, on_delete=models.SET_NULL)
    Assignment_Date = models.DateField(null=True)
    Note = models.TextField(null=True)
   
class Organizations(models.Model):
    OrganizationID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)
    Type = models.ForeignKey("Types", null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.Title

class Types(models.Model):
    TypeID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)
    def __str__(self):
        return self.Title
    
class Status(models.Model):
    StatusID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)
    def __str__(self):
        return self.Title
    
class LifeCycle(models.Model):
    LifeCycleID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)   
    def __str__(self):
        return self.Title

class Gender(models.Model):
    GenderID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)
    def __str__(self):
        return self.Title
    
class Ethnicity(models.Model):
    EthnicityID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)
    def __str__(self):
        return self.Title
    
class Roles(models.Model):
    RoleID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)
    def __str__(self):
        return self.Title
    
