# Generated by Django 4.0 on 2022-01-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_bike_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikeinstance',
            name='color',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]