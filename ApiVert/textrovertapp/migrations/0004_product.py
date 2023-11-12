# Generated by Django 4.2.7 on 2023-11-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textrovertapp', '0003_alter_textrovertappdata_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=99.99, max_digits=15)),
            ],
        ),
    ]