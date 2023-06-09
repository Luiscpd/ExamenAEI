# Generated by Django 4.2 on 2023-05-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospedaje', '0003_delete_huespedes_remove_datoshuesped_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='precionoche',
            old_name='date',
            new_name='checkin',
        ),
        migrations.AddField(
            model_name='precionoche',
            name='checkout',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='datoshuesped',
            name='DPI',
            field=models.FloatField(default=0, primary_key=True, serialize=False),
        ),
    ]
