# Generated by Django 2.2 on 2019-04-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testDjango_app', '0003_auto_20190416_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]
