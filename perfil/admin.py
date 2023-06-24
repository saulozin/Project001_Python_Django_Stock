from django.contrib import admin
from perfil import models

# Register your models here.

@admin.register(models.Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'registration',
        'user',
        'phone',
    )
    ordering = ('-id',)
    search_fields = ('registration', 'user.first_name', 'user.last_name', 'user.email',)
    list_per_page = 10
    list_max_show_all = 500
    list_editable = ('phone',)
    list_display_links = ('id', 'registration',)
