# Generated by Django 3.1.4 on 2020-12-21 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='age',
        ),
        migrations.RemoveField(
            model_name='club',
            name='category',
        ),
        migrations.DeleteModel(
            name='Age',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Club',
        ),
    ]