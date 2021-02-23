from django.contrib import admin
from .models import Study, KitOrder


class KitOrderList(admin.ModelAdmin):
    list_display = ( 'type', 'web_address', 'description' )
    list_filter = ( 'type', 'web_address')
    search_fields = ('type', )
    ordering = ['web_address']


class StudyList(admin.ModelAdmin):
    list_display = ( 'IRB_number', 'pet_name', 'status' )
    list_filter = ( 'IRB_number', 'start_date')
    search_fields = ('IRB_number', )
    ordering = ['IRB_number']


admin.site.register(Study)
admin.site.register(KitOrder)
