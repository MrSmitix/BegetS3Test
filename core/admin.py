from django.contrib import admin

from .models import Picture, Document


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    ...


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    ...
