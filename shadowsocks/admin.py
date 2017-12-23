from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'level', 'balance', ]
    search_fields = ['username', 'email', 'pk']


class PurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ['info','user', 'money', 'purchtime', ]
    search_fields = ['user', ]


class InviteCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'time_created', 'isused', 'type']
    search_fields = ['code']


class AliveipAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'ip_address', 'time']


class MoneyCodeAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'isused']


class AlipayAdmin(admin.ModelAdmin):
    list_display = ['username', 'info_code', 'amount', 'money_code', 'time', ]
    search_fields = ['info_code', ]


class AlipayRequestAdmin(admin.ModelAdmin):
    list_display = ['username', 'amount', 'info_code', 'time', ]


class DonateAdmin(admin.ModelAdmin):
    list_display = ['user', 'money', 'time', ]


class NodeAdmin(admin.ModelAdmin):
    list_display = ['node_id', 'name', 'level', 'show', ]


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'transfer', 'money', 'level', ]


class NodeOnlineAdmin(admin.ModelAdmin):
    list_display = ['node_id', 'online_user']


# Register your models here.
admin.site.register(models.User, UserAdmin)
admin.site.register(models.InviteCode, InviteCodeAdmin)
admin.site.register(models.Node, NodeAdmin)
admin.site.register(models.Donate, DonateAdmin)
admin.site.register(models.MoneyCode, MoneyCodeAdmin)
admin.site.register(models.Shop, ShopAdmin)
admin.site.register(models.PurchaseHistory, PurchaseHistoryAdmin)
admin.site.register(models.AlipayRecord, AlipayAdmin)
admin.site.register(models.AlipayRequest, AlipayRequestAdmin)
admin.site.register(models.NodeOnlineLog, NodeOnlineAdmin)
admin.site.register(models.NodeInfoLog)
admin.site.register(models.Announcement)
admin.site.register(models.Ticket)
