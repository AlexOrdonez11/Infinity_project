# Generated by Django 3.1.4 on 2020-12-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infinity', '0002_orden_trans_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
