# Generated by Django 5.0.3 on 2024-07-01 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
