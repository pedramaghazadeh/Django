# Generated by Django 2.1.5 on 2019-02-08 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0006_auto_20190207_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
