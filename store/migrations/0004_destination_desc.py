# Generated by Django 4.2.5 on 2023-10-07 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_destination_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='desc',
            field=models.TextField(default='Loading...'),
            preserve_default=False,
        ),
    ]
