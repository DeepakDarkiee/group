# Generated by Django 3.1.5 on 2021-03-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210310_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='call',
            field=models.IntegerField(default=True),
        ),
    ]