# Generated by Django 4.2.5 on 2023-09-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSangrah', '0002_contact_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='offers_img')),
            ],
        ),
    ]
