# Generated by Django 5.0.1 on 2024-02-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_alter_page_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]