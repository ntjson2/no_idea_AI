# Generated by Django 4.0.8 on 2022-10-24 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='phrase',
            field=models.TextField(null=True),
        ),
    ]
