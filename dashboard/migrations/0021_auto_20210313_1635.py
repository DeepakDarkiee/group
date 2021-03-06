# Generated by Django 3.1.5 on 2021-03-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_auto_20210313_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='intern',
            name='enddate',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='intern',
            name='intern_cource',
            field=models.CharField(blank=True, default=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='intern',
            name='startdate',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='internattendance',
            name='half_day',
            field=models.CharField(default='No', max_length=100),
        ),
        migrations.AddField(
            model_name='trainee',
            name='enddate',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='trainee',
            name='startdate',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='trainee',
            name='trainee_cource',
            field=models.CharField(blank=True, default=True, max_length=100, null=True),
        ),
    ]
