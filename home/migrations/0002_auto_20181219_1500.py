# Generated by Django 2.1.4 on 2018-12-19 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalheader',
            name='bg_img',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='generalheader',
            name='content_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
