# Generated by Django 3.0.2 on 2020-03-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20200317_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
