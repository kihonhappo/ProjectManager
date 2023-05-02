from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Projects)
admin.site.register(models.BacklogItems)
admin.site.register(models.WorkEvents)
admin.site.register(models.Stakeholders)
admin.site.register(models.Assignments)
admin.site.register(models.Organizations)
admin.site.register(models.Types)
admin.site.register(models.Status)
admin.site.register(models.LifeCycle)
admin.site.register(models.Gender)
admin.site.register(models.Ethnicity)
admin.site.register(models.Roles)