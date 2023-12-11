# Generated by Django 4.2.8 on 2023-12-11 10:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название меню')),
                ('slug', models.SlugField(unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+\\Z')], verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='Submenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название меню')),
                ('slug', models.SlugField(unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+\\Z')], verbose_name='Слаг')),
                ('menu', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='submenu', to='menu.menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.submenu')),
            ],
            options={
                'verbose_name': 'Submenu',
                'verbose_name_plural': 'Submenus',
            },
        ),
    ]