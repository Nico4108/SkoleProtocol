# Generated by Django 3.2.9 on 2021-11-19 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('year_started', models.CharField(max_length=4)),
                ('Course_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
            options={
                'db_table': 'Class',
            },
        ),
    ]
