# Generated by Django 2.1.4 on 2019-01-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenantdetail',
            name='emergency_contact_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tenantdetail',
            name='emergency_contact_relationship',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tenantdetail',
            name='occupation',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tenantdetail',
            name='relationship_status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
