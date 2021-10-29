# Generated by Django 3.2.4 on 2021-06-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20210630_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('confirmed', 'Confirmed'), ('delivered', 'Delivered'), ('canceled', 'Canceled')], default='ordered', max_length=10),
        ),
    ]
