# Generated by Django 4.2 on 2023-05-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_assignments_project_alter_assignments_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ethnicity',
            name='EthnicityID',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
