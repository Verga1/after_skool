# Generated by Django 3.1.4 on 2020-12-29 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivery_cost',
            new_name='discount',
        ),
    ]