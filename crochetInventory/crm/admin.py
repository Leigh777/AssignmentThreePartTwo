from django.contrib import admin
from .models import CrochetHook, Yarn, Gift


class CrochetHookList(admin.ModelAdmin):
    list_display = ('crochethook_size', 'count', 'material')
    list_filter = ('crochethook_size', 'material')
    search_fields = ('crochethook_size',)
    ordering = ['crochethook_size']


class YarnList(admin.ModelAdmin):
    list_display = ('crochethook_size', 'yarn_color', 'yarn_texture', 'yarn_amount')
    list_filter = ('crochethook_size', 'yarn_color')
    search_fields = ('crochethook_size',)
    ordering = ['crochethook_size']


class GiftList(admin.ModelAdmin):
    list_display = ('crochethook_size', 'yarn_color', 'recipient_name', 'gift_size')
    list_filter = ('crochethook_size', 'recipient_name')
    search_fields = ('crochethook_size',)
    ordering = ['crochethook_size']


admin.site.register(CrochetHook, CrochetHookList)
admin.site.register(Yarn, YarnList)
admin.site.register(Gift, GiftList)
