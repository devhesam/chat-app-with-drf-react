from django.contrib import admin

from server.models import Server, Category, Channel


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['id', 'name']


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner', 'category', 'description', 'is_active', 'created_time', 'updated_time']
    list_editable = ['is_active']
    search_fields = ['id', 'name']
    list_filter = ['is_active', 'created_time', 'updated_time']
    raw_id_fields = ['owner', 'category']
    date_hierarchy = 'created_time'
    readonly_fields = ['created_time', 'updated_time']
    filter_horizontal = ['member']


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner', 'topic', 'server', 'is_active', 'created_time', 'updated_time']
    list_editable = ['is_active']
    search_fields = ['id', 'name']
    list_filter = ['is_active', 'created_time', 'updated_time']
    raw_id_fields = ['owner', 'server']
    date_hierarchy = 'created_time'
    readonly_fields = ['created_time', 'updated_time']
