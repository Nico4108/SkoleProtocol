# Generated by Django 3.2.9 on 2021-12-16 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
            options={
                'db_table': 'Subject',
            },
        ),
        migrations.CreateModel(
            name='StudentHasSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('subject_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subject.subject')),
            ],
            options={
                'db_table': 'StudentHasSubject',
            },
        ),
    ]
