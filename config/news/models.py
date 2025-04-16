from django.db import models
from django.core.validators import MinLengthValidator
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse


class Tag(models.Model):
    """Модель для тэгов"""
    name = models.CharField(
        'Название тэга',
        max_length=50,
        unique=True,
        validators=[MinLengthValidator(2, "Тег должен быть не короче 2 символов")]
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']

    def __str__(self):
        return self.name



class News(models.Model):
    """Модель статьи"""
    title = models.CharField(
        'Название статьи',
        max_length=200,
        validators=[MinLengthValidator(5, "Заголовок должен быть не короче 5 символов")]
    )

    description = models.TextField(
        'Краткое описание',
        max_length=300
    )

    slug = models.SlugField(
        'slug',
        max_length=200,
        unique=True
    )

    content = CKEditor5Field(
        'Текст статьи',
        config_name='extends'
    )

    image = models.ImageField(
        'Обложка статьи',
        upload_to='news_images/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        'Создание статьи',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Обновление статьи',
        auto_now=True
    )

    is_published = models.BooleanField(
        'Опубликовать?',
        default=True
    )

    views = models.PositiveIntegerField(
        'Счетчик просмотров',
        default=0
    )

    tags = models.ManyToManyField(
        Tag,
        related_name='news'
    )

    launcher_image = models.ImageField(
        'Фотография для лаунчера',
        help_text="Формат 480x150",
        upload_to='news_images/',
        blank=True,
        null=True
    )


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
        ]


    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

    # проверка новый пост или нет.
    def is_new(self):
        return (timezone.now() - self.created_at) < timedelta(days=7)


    # счетчик просмотров - логика
    def increment_views(self):
        self.views += 1
        self.save(update_fields=['views'])
