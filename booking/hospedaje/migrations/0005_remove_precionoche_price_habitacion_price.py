# Generated by Django 4.2 on 2023-05-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospedaje', '0004_rename_date_precionoche_checkin_precionoche_checkout_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='precionoche',
            name='price',
        ),
        migrations.AddField(
            model_name='habitacion',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
