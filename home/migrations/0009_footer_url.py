# Generated by Django 2.1.4 on 2018-12-21 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_footer_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]