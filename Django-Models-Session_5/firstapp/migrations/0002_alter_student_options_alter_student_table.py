# Generated by Django 4.1 on 2022-08-20 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['number'], 'verbose_name_plural': 'Student_List'},
        ),
        migrations.AlterModelTable(
            name='student',
            table='Student_List',
        ),
    ]
