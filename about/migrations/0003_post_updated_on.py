# Generated by Django 4.2.16 on 2024-12-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_post_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
