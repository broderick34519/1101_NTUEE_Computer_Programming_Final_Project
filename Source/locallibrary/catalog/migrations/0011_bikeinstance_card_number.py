# Generated by Django 4.0 on 2022-01-17 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_bikeinstance_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikeinstance',
            name='Card_number',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
