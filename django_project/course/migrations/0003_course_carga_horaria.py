# Generated by Django 3.2.9 on 2021-11-21 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20211016_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='carga_horaria',
            field=models.IntegerField(default=8825436587),
            preserve_default=False,
        ),
    ]
