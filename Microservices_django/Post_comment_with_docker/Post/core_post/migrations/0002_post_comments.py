# Generated by Django 5.0.4 on 2024-07-01 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.TextField(default='[]'),
        ),
    ]