# Generated by Django 4.2.5 on 2023-09-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSangrah', '0009_alter_xerox_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='DryFruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='dryfruit_img')),
                ('desc', models.CharField(max_length=100)),
                ('price', models.FloatField(max_length=6)),
            ],
        ),
        migrations.AlterField(
            model_name='xerox',
            name='file',
            field=models.FileField(default=1, upload_to='document'),
            preserve_default=False,
        ),
    ]