# Generated by Django 2.1.4 on 2019-01-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20190107_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generalheader',
            old_name='content_text',
            new_name='text1',
        ),
        migrations.AddField(
            model_name='generalheader',
            name='text2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generalheader',
            name='text3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
