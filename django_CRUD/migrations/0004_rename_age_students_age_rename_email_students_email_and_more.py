# Generated by Django 4.1.7 on 2023-04-05 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_CRUD', '0003_students_gender_alter_students_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='Name',
            new_name='name',
        ),
    ]
