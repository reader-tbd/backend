# Generated by Django 3.2.3 on 2021-06-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readmanga_parser', '0005_auto_20210604_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='alt_title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
