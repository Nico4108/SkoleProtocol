# Generated by Django 3.2.9 on 2021-11-22 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subject', '0001_initial'),
        ('keaclass', '0001_initial'),
        ('attendanceCode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancelog',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.subject'),
        ),
        migrations.AddField(
            model_name='attendancelog',
            name='username_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attendancecode',
            name='keaclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keaclass.class'),
        ),
        migrations.AddField(
            model_name='attendancecode',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.subject'),
        ),
    ]
