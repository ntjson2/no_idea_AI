# Generated by Django 4.0.8 on 2022-11-15 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='urls',
            field=models.CharField(default='1', max_length=1000),
            preserve_default=False,
        ),
    ]
