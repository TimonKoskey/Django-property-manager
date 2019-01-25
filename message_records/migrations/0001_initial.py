# Generated by Django 2.1.4 on 2019-01-13 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('sent_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_details', to='app_users.ExtendedUserDetail')),
                ('sent_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_details', to='app_users.ExtendedUserDetail')),
            ],
        ),
    ]
