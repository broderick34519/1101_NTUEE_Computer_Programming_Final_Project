# Generated by Django 3.2.9 on 2021-12-20 11:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief description of the bicycle', max_length=1000)),
                ('isbn', models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, unique=True, verbose_name='Bike ID')),
            ],
        ),
        migrations.CreateModel(
            name='BikeInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular bike across whole library', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Bike availability', max_length=1)),
                ('bike', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.bike')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter a bike genre (e.g. Science Fiction)', max_length=200),
        ),
        migrations.RenameModel(
            old_name='Author',
            new_name='Owner',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
        migrations.AddField(
            model_name='bike',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this bicycle', to='catalog.Genre'),
        ),
        migrations.AddField(
            model_name='bike',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.owner'),
        ),
    ]
