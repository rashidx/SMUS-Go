# Generated by Django 2.1.7 on 2019-02-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiritdashboard', '0017_mission_xp_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='missionkey',
            name='one_use',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='missionkey',
            name='times_used',
            field=models.IntegerField(default=0),
        ),
    ]
