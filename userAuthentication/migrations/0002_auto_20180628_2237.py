# Generated by Django 2.0.6 on 2018-06-28 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAuthentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='User_details',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='superadministrator',
            name='User_details',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
