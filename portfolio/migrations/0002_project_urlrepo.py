# Generated by Django 4.1.7 on 2023-02-16 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='urlrepo',
            field=models.URLField(blank=True),
        ),
    ]