# Generated by Django 5.0.4 on 2024-05-08 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='year1',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='year2',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
    ]
