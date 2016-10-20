# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 06:13
from __future__ import unicode_literals

from django.db import migrations

def load_groups(apps, schema_editor):
    from DCODtesttask.settings import BASE_DIR
    from os import path
    import json

    json_file_path = path.join(BASE_DIR, 'chart/static/2CuNPefD.json')
    with open(json_file_path) as data_file:
        data = json.load(data_file)

    Group = apps.get_model('chart', 'Group')
    City = apps.get_model('chart', 'City')

    groups = []
    for line in data['data']:
        group, parameter, value = line['Область'], line['Город'], line['Значение']
        if group not in groups:
            print(group)
            new_group = Group(name=group)
            new_group.save()
            groups.append(group)
        new_city = City(group=Group.objects.get(name=group), name=parameter, value=value.split('.')[0])
        new_city.save()

class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0002_auto_20161020_0856'),
    ]

    operations = [
        migrations.RunPython(load_groups)
    ]