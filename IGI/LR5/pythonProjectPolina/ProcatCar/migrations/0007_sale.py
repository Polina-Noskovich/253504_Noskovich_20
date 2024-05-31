# Generated by Django 5.0.6 on 2024-05-16 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProcatCar', '0006_vac'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale', models.CharField(max_length=100, verbose_name='Название')),
                ('saleopis', models.CharField(max_length=300, verbose_name='Полное описание')),
            ],
        ),
    ]