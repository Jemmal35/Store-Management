# Generated by Django 4.1.4 on 2023-10-29 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0007_alter_product_entrance_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Solled',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['Entrance_Date']},
        ),
    ]