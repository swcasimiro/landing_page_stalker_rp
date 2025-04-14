from ckeditor.fields import RichTextField
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.translation import gettext_lazy as _

class Launcher(models.Model):
    name = models.CharField(
        'Версия лаунчера',
        max_length=6
    )
    file = models.FileField(
        'Installer',
        upload_to='uploads_model'
    )
    cache = models.FileField(
        'Cache',
        upload_to='uploads_model'
    )

    def __str__(self):
        return f"Stalker Role Play Launcher v{self.name}"


class RulesProject(models.Model):
    name_rules = models.CharField(
        'Название правил',
        max_length=160
    )
    rules_description = CKEditor5Field(
        'Content',
        config_name='extends'
    )

    def __str__(self):
        return f"{self.id} {self.name_rules}"


