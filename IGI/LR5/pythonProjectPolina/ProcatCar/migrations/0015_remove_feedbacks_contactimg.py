# Generated by Django 5.0.6 on 2024-05-27 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProcatCar', '0014_remove_feedbacks_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbacks',
            name='contactimg',
        ),
    ]
