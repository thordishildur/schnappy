from django.contrib import admin

# Register your models here.
from chat.models import Schnap, Friendship

class SchnapAdmin(admin.ModelAdmin):
    list_display = ('sender', 'sent_at', 'description')
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('creator', 'receiver', 'created')
admin.site.register(Schnap, SchnapAdmin)
admin.site.register(Friendship, FriendshipAdmin)
