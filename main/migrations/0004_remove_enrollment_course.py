# Generated by Django 5.1.3 on 2024-11-26 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_course_is_active_remove_student_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='course',
        ),
    ]
