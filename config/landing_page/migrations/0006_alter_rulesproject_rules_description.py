# Generated by Django 5.1.7 on 2025-04-13 23:29

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0005_rulesproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rulesproject',
            name='rules_description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Content'),
        ),
    ]
