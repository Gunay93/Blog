# Generated by Django 2.1.4 on 2018-12-24 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_generalheader_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalheader',
            name='bg_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
