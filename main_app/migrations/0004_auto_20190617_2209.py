# Generated by Django 2.2 on 2019-06-17 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190617_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='winery',
            name='desc',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='winery',
            name='price',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
