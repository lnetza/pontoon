# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 19:14
from __future__ import unicode_literals

from django.db import migrations


def create_pm_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    group, created = Group.objects.get_or_create(name='project_managers')

    if created:
        project_content_type, _ = ContentType.objects.get_or_create(app_label='base', model='project')
        can_manage_project, _ = Permission.objects.get_or_create(content_type=project_content_type, codename='can_manage_project')
        group.permissions.add(can_manage_project)


def remove_pm_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.get(name='project_managers').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0088_auto_20170310_2150'),
    ]

    operations = [
        migrations.RunPython(create_pm_groups, remove_pm_groups),
    ]