# Generated by Django 4.1.7 on 2023-09-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSangrah', '0013_alter_dailyneed_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stationary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='stationary_img')),
                ('desc', models.CharField(max_length=100)),
                ('price', models.FloatField(max_length=6)),
            ],
        ),
        migrations.AlterField(
            model_name='electronic',
            name='image',
            field=models.ImageField(upload_to='electronic_img'),
        ),
    ]