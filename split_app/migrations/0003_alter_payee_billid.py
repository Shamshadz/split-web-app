# Generated by Django 4.1 on 2022-08-24 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('split_app', '0002_payee_bill_created_at_delete_payees_payee_billid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payee',
            name='billId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='split_app.bill'),
        ),
    ]
