# Generated by Django 3.2.7 on 2021-09-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_remove_dojo_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='dojo antiguo'),
            preserve_default=False,
        ),
    ]