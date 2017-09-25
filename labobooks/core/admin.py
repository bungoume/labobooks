from django.contrib import admin

from core import models


admin.site.register(models.MyBook)
admin.site.register(models.BookInfo)
admin.site.register(models.Organization)
admin.site.register(models.OrganizationMember)
