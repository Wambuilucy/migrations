# Generated by Django 3.1.2 on 2020-10-12 12:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gallery.category'),
            preserve_default=False,
        ),
    ]
