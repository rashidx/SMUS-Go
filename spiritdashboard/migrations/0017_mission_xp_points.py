# Generated by Django 2.1.7 on 2019-02-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiritdashboard', '0016_auto_20181225_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='xp_points',
            field=models.IntegerField(default=5),
        ),
    ]
