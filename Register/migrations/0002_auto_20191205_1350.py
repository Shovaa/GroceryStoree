# Generated by Django 2.2.8 on 2019-12-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='ConfrimPassword',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='ContactInfo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='FullName',
            field=models.TextField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
