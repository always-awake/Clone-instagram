# Generated by Django 2.0.6 on 2018-07-11 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0007_image_tags'),
        ('notifications', '0003_auto_20180710_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications_comment', to='images.Comment'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications_image', to='images.Image'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
