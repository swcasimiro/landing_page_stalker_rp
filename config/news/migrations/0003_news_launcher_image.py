# Generated by Django 5.1.7 on 2025-04-16 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_description_alter_news_is_published_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='launcher_image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images/', verbose_name='Фотография для лаунчера'),
        ),
    ]
