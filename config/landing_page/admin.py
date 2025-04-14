from django.contrib import admin
from .models import Launcher, RulesProject
from django.contrib import admin
from django_ckeditor_5.widgets import CKEditor5Widget
from django.db import models

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget},
    }

admin.site.register(Launcher)
admin.site.register(RulesProject, ArticleAdmin)




