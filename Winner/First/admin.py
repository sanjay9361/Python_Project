from django.contrib import admin

from . import models as M
# Register your models here.

admin.site.register(M.Create)

admin.site.register(M.Types)