from django.contrib import admin
from .models import Menu, Submenu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')


@admin.register(Submenu)
class SubAdmin(admin.ModelAdmin):
    list_display = ('menu', 'parent')
    search_fields = ('menu', 'parent')
    # fieldsets = (
    #     ('Add new item', {
    #         'description': "Parent should be a menu or item",
    #         'fields': (('menu', 'parent'), 'name', 'slug')
    #         }),
    # )
