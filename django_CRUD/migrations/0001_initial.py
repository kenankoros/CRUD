# Generated by Django 4.1.7 on 2023-04-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('Age', models.IntegerField(max_length=30)),
            ],
        ),
    ]
