# Generated by Django 4.2.5 on 2023-09-16 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('desc', models.CharField(max_length=100)),
                ('price', models.FloatField(max_length=6)),
            ],
        ),
    ]
