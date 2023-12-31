# Generated by Django 4.1.4 on 2023-09-01 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=50)),
                ('Lname', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Price', models.FloatField()),
                ('Quantity', models.IntegerField()),
                ('Entrance_Date', models.DateTimeField(auto_now=True)),
                ('Expired_Date', models.DateTimeField()),
                ('Approved_By', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webApp.user')),
            ],
        ),
    ]
