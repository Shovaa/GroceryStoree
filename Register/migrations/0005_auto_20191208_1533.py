# Generated by Django 2.2.8 on 2019-12-08 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0004_items_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='SellingPrice',
            new_name='Price',
        ),
    ]
