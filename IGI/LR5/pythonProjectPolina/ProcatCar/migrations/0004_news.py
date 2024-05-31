# Generated by Django 5.0.6 on 2024-05-16 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProcatCar', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newscrat', models.CharField(max_length=100, verbose_name='Краткая')),
                ('news', models.CharField(max_length=300, verbose_name='Полная')),
                ('newsimg', models.ImageField(upload_to='static', verbose_name='Картинка')),
            ],
        ),
    ]
