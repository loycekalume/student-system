# Generated by Django 5.1.3 on 2024-11-26 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_course_created_at_course_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]