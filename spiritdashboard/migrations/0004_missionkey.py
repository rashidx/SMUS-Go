# Generated by Django 2.1.4 on 2018-12-22 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spiritdashboard', '0003_auto_20181222_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissionKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=10)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spiritdashboard.Mission')),
            ],
        ),
    ]
