# Generated by Django 4.1.7 on 2023-04-05 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_CRUD', '0002_alter_students_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='gender',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='Name',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
