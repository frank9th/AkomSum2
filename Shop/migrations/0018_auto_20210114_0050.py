# Generated by Django 3.1.5 on 2021-01-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0017_placedorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placedorder',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]