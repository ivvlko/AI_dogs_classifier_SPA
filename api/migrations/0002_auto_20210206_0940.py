# Generated by Django 3.1.6 on 2021-02-06 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageclassification',
            name='url',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]
