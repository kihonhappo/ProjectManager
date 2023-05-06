from django.db import models
from django.contrib.auth.models import User

# Django Data Models - Are the single, definitive source of information about your data. They contain the essential fields and behaviors of the data 
# you’re storing. Generally, each model maps to a single database table.

# Each model is a Python class that subclasses django.db.models.Model.
# Each attribute of the model represents a database field.
# Django gives you an automatically-generated database-access API.

# Project Model - This is the topmost object for all other objects
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
# Backlog Items Model - This is the second highest object and is associated with the Project Object
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

# Work Event Model - This is the third highest object and is a child of the Backlog Item and grandchild of the Project Object
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

# Stakeholder Model - This model is used in the Project, Backlog Item as well as the Work Event objects  
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

# Assignments Model - This is a linking table between the Project and Stakeholder Objects
class Assignments(models.Model):
    AssignmentID = models.AutoField(primary_key=True, editable=False)
    Project = models.ForeignKey("Projects", null=True, on_delete=models.SET_NULL)
    Stakeholder = models.ForeignKey("Stakeholders", null=True, on_delete=models.SET_NULL)
    Role = models.ForeignKey("Roles", null=True, on_delete=models.SET_NULL)
    Assignment_Date = models.DateField(null=True)
    Note = models.TextField(null=True)
 
# Organization Model - This model is used to define stakeholder Entity identity. The organization is attached to the Stakeholder  
class Organizations(models.Model):
    OrganizationID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)
    Type = models.ForeignKey("Types", null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.Title

# Work Event Model - This is the third highest object and is a child of the Backlog Item and grandchild of the Project Object. The
# Work Event is used for each time any type of work is performed on a Backlog Item 
class Types(models.Model):
    TypeID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)
    def __str__(self):
        return self.Title

# Status Model - This model is a helper table that defines the status for each of the different Higher objects. Projects and Backlog Items  
class Status(models.Model):
    StatusID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)
    def __str__(self):
        return self.Title

# LifeCycle Model - This model is used to define the current life cycle for the Project Object. There will be a Kanban or scrum board that 
# will be set up as a visualization to track the progress for multiple projects  
class LifeCycle(models.Model):
    LifeCycleID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)   
    def __str__(self):
        return self.Title

# Gender Model - This model is a helper table that defines the gender for Stakeholders and users.
class Gender(models.Model):
    GenderID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)
    def __str__(self):
        return self.Title

# Ethnicity Model - This model is a helper table that defines the ethnicity for Stakeholders and users.
class Ethnicity(models.Model):
    EthnicityID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)
    def __str__(self):
        return self.Title
    
# Roles Model - This model is a helper table that defines the role for Stakeholders.   
class Roles(models.Model):
    RoleID = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True)
    def __str__(self):
        return self.Title
    
