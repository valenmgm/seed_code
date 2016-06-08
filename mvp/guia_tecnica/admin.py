from django.contrib import admin

# Register your models here.

from . import models

admin.sites.register(models.GuiaTecnica)
