# Generated by Django 3.2.3 on 2021-06-29 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0017_auto_20210618_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('link', models.URLField(max_length=2000)),
                ('number', models.IntegerField()),
                ('volume', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='manga',
            name='volumes',
        ),
        migrations.AddField(
            model_name='manga',
            name='volumes',
            field=models.ManyToManyField(to='parse.Chapter'),
        ),
    ]
