# Generated by Django 3.2.4 on 2021-06-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210630_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='Quweisna', max_length=100),
        ),
    ]
