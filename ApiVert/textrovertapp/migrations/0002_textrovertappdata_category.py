# Generated by Django 4.2.7 on 2023-11-09 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textrovertapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textrovertappdata',
            name='category',
            field=models.CharField(default='action', max_length=200),
        ),
    ]