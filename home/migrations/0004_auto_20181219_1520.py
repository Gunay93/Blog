# Generated by Django 2.1.4 on 2018-12-19 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20181219_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generalheader',
            old_name='page_type',
            new_name='page_name',
        ),
    ]
