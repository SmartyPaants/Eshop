# Generated by Django 4.0.4 on 2022-05-22 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_customer_alter_product_descriptions_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
