# Generated by Django 4.2 on 2023-05-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospedaje', '0002_rename_datos_datoshuesped'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Huespedes',
        ),
        migrations.RemoveField(
            model_name='datoshuesped',
            name='id',
        ),
        migrations.AddField(
            model_name='datoshuesped',
            name='DPI',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='datoshuesped',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='precionoche',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='precionoche',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='precionoche',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]