# Generated by Django 3.2.4 on 2021-06-30 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_customer_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='delivery_man',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.deliveryman'),
        ),
    ]