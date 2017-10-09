from django.contrib import admin

from core import models


class OrganizationMember(admin.ModelAdmin):
    raw_id_fields = ('organization', 'user',)


class OrganizationMemberInline(admin.TabularInline):
    model = models.OrganizationMember
    raw_id_fields = ('user',)
    extra = 1


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_slug', 'id')
    # ordering = ("name",)
    search_fields = ['name', 'id_slug']
    readonly_fields = ('created_at', 'updated_at')
    inlines = (OrganizationMemberInline, )


class MyBookAdmin(admin.ModelAdmin):
    list_display = ('organization', 'book_info', 'id')
    readonly_fields = ('created_at', 'updated_at')
    raw_id_fields = ('organization', 'book_info',)


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title')
    # ordering = ("name",)
    search_fields = ['isbn', 'title']
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(models.MyBook, MyBookAdmin)
admin.site.register(models.BookInfo, BookInfoAdmin)
admin.site.register(models.Organization, OrganizationAdmin)
admin.site.register(models.OrganizationMember, OrganizationMember)
