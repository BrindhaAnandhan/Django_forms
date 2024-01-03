# Generated by Django 4.2.7 on 2024-01-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Experience', models.IntegerField()),
                ('Mobile', models.IntegerField(unique=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Portfolio', models.URLField()),
            ],
        ),
    ]
