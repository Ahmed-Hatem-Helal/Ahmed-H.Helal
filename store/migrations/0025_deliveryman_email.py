# Generated by Django 3.2.4 on 2021-06-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_alter_cartitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryman',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
    ]
