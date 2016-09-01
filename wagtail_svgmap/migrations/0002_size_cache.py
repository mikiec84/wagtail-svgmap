# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-01 12:35
from __future__ import unicode_literals

from django.db import migrations, models
from django.db.models import Q


def update_caches(apps, schema_editor):
    from wagtail_svgmap.models import ImageMap
    for image_map in ImageMap.objects.filter(Q(_width_cache=0) | Q(_height_cache=0)).iterator():
        image_map.recache_svg(save=True)


class Migration(migrations.Migration):
    dependencies = [
        ('wagtail_svgmap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemap',
            name='_height_cache',
            field=models.FloatField(db_column='height_cache', default=0, editable=False),
        ),
        migrations.AddField(
            model_name='imagemap',
            name='_width_cache',
            field=models.FloatField(db_column='width_cache', default=0, editable=False),
        ),
        migrations.RunPython(
            update_caches,
            reverse_code=migrations.RunPython.noop,
        )
    ]