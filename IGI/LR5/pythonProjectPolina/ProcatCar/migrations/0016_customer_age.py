# Generated by Django 5.0.4 on 2024-05-31 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProcatCar', '0015_remove_feedbacks_contactimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.PositiveIntegerField(default=20, verbose_name='Возраст'),
            preserve_default=False,
        ),
    ]
