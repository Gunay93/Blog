# Generated by Django 2.1.4 on 2019-01-07 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20181224_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]