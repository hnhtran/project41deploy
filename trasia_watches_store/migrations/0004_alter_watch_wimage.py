# Generated by Django 3.2.14 on 2022-07-31 20:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trasia_watches_store', '0003_watch_wimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='wimage',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]