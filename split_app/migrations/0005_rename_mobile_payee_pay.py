# Generated by Django 4.1 on 2022-08-25 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('split_app', '0004_bill_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payee',
            old_name='mobile',
            new_name='pay',
        ),
    ]
