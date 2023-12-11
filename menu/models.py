from django.core.validators import RegexValidator
from django.db import models


class Menu(models.Model):
    """Класс для меню."""
    name = models.CharField(
        verbose_name='Название меню',
        unique=True,
        max_length=50)
    slug = models.SlugField(
        verbose_name='Слаг',
        unique=True,
        validators=[
            RegexValidator(r'^[\w.@+-]+\Z')
        ])

    class Meta:
        verbose_name = 'Menu'

    def __str__(self):
        return self.name


class Submenu(models.Model):
    """Класс для подменю."""
    name = models.CharField(
        verbose_name='Название подменю',
        max_length=50)
    slug = models.SlugField(
        verbose_name='Слаг',
        unique=True,
        validators=[
            RegexValidator(r'^[\w.@+-]+\Z')
        ])
    menu = models.ForeignKey(
        Menu,
        blank=True,
        verbose_name='Название меню',
        related_name='submenu',
        on_delete=models.CASCADE,
        )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        verbose_name='Родитель',
        related_name='children',
        on_delete=models.CASCADE,
        )
    url = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='URL',
    )

    class Meta:
        verbose_name = 'Submenu'

    def __str__(self):
        return self.name
