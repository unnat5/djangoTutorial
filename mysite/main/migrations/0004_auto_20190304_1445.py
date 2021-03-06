# Generated by Django 2.1.5 on 2019-03-04 14:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190304_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 4, 14, 45, 32, 936854, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorialcategory',
            name='category_slug',
            field=models.CharField(max_length=200),
        ),
    ]
