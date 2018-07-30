# Generated by Django 2.0.6 on 2018-06-29 00:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userAuthentication', '0002_auto_20180628_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.FileField(upload_to='')),
                ('User_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tenant',
            name='Amount_paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tenant',
            name='Current_month_payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tenant',
            name='Entry_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='Rent_payment_date',
            field=models.DateTimeField(null=True),
        ),
    ]
