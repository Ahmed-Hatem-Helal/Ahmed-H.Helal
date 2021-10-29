# Generated by Django 3.2.4 on 2021-06-30 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_cartitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='status',
        ),
        migrations.AddField(
            model_name='shipping',
            name='status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('confirmed', 'Confirmed'), ('delivered', 'Delivered')], default='ordered', max_length=10),
        ),
    ]
