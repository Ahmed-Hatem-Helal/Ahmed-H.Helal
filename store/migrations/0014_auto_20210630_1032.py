# Generated by Django 3.2.4 on 2021-06-30 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_shipping_delivery_man'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ManyToManyField(to='store.Cart'),
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='order',
        ),
        migrations.AddField(
            model_name='shipping',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.cart'),
        ),
    ]
