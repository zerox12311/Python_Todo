# Generated by Django 2.0.5 on 2018-05-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='tag',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
