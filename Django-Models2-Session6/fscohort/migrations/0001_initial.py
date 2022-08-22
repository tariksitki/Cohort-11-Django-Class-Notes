# Generated by Django 4.1 on 2022-08-22 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Adi')),
                ('last_name', models.CharField(max_length=50, verbose_name='Soyadi')),
                ('number', models.IntegerField(verbose_name='Numara')),
            ],
        ),
    ]
