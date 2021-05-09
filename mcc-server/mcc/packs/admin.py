from django.contrib import admin

from .models import CitPack


class CitPackAdmin(admin.ModelAdmin):
    list_display = ("name", "official_site")


admin.site.register(CitPack, CitPackAdmin)
