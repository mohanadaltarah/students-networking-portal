# Generated by Django 5.0 on 2023-12-23 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_student_studentid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
    ]
