# Generated by Django 4.1 on 2022-08-29 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name_plural': 'Todoss'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('1', '😂'), ('1', '😊'), ('1', '🤣'), ('1', '😒'), ('1', '😁')], max_length=30),
        ),
        migrations.AlterModelTable(
            name='todo',
            table='Todos_Table',
        ),
    ]
