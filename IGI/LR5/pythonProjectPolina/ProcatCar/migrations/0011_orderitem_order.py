# Generated by Django 5.0.6 on 2024-05-17 04:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProcatCar', '0010_remove_orderitem_object_remove_car_code_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество объекта')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProcatCar.car')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата заказа')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('cars', models.ManyToManyField(blank=True, to='ProcatCar.orderitem')),
            ],
        ),
    ]