# Generated by Django 3.2.3 on 2021-06-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("readmanga_parser", "0004_auto_20210603_1543"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="illustrator",
            name="name",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="manga",
            name="image_url",
            field=models.URLField(default="", verbose_name="thumbnail url"),
        ),
        migrations.AlterField(
            model_name="manga",
            name="status",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="manga",
            name="title",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="manga",
            name="year",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="screenwriter",
            name="name",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="translator",
            name="name",
            field=models.TextField(unique=True),
        ),
    ]
