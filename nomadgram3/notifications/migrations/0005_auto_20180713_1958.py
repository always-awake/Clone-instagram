# Generated by Django 2.0.6 on 2018-07-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20180711_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]