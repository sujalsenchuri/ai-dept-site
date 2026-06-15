from django.contrib import admin
from django.utils.html import format_html
from django.conf import settings
from .models import TeamMember, ServiceCard, Faculty, Club



@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'created_at', 'image_preview')
    search_fields = ('name', 'position')
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'position', 'bio')
        }),
        ('Media', {
            'fields': ('photo',)
        }),
        ('Social Links', {
            'fields': ('instagram_url', 'linkedin_url', 'facebook_url'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.photo:
            # build static URL to the image path stored in the photo field
            url = settings.STATIC_URL.rstrip('/') + '/images/' + obj.photo.lstrip('/')
            return format_html('<img src="{}" style="height:80px;border-radius:6px;"/>', url)
        return "-"

    image_preview.short_description = 'Photo'


@admin.register(ServiceCard)
class ServiceCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'link_text', 'image_preview')
    search_fields = ('title', 'description', 'link_text')
    readonly_fields = ('created_at', 'updated_at', 'image_preview')
    fieldsets = (
        ('Card Content', {
            'fields': ('title', 'description', 'link_url', 'link_text')
        }),
        ('Media', {
            'fields': ('image', 'image_preview')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            url = settings.STATIC_URL.rstrip('/') + '/images/' + obj.image.lstrip('/')
            return format_html('<img src="{}" style="height:80px;border-radius:6px;"/>', url)
        return "-"

    image_preview.short_description = 'Image Preview'


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'icon', 'created_at')
    list_editable = ('order',)
    search_fields = ('name', 'description')
    ordering = ('order', 'name')
    
    fieldsets = (
        ('Club Information', {
            'fields': ('name', 'description', 'order')
        }),
        ('Icon & Link', {
            'fields': ('icon', 'link_url', 'link_text'),
            'description': 'Icon should be a Bootstrap Icon class name (e.g., bi-cpu, bi-robot, bi-camera-video)'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order', 'photo_preview')
    list_editable = ('order',)
    search_fields = ('name', 'position')
    ordering = ('order', 'name')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'position', 'order')
        }),
        ('Photo', {
            'fields': ('photo', 'photo_preview')
        }),
        ('Research', {
            'fields': ('research_area', 'research_area_2', 'research_area_3')
        }),
        ('Contact Information', {
            'fields': ('email', 'linkedin_url', 'website_url')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('photo_preview', 'created_at', 'updated_at')
    
    def photo_preview(self, obj):
        if obj.photo:
            url = settings.STATIC_URL.rstrip('/') + '/images/' + obj.photo.lstrip('/')
            return format_html('<img src="{}" style="height:100px;border-radius:6px;"/>', url)
        return "No photo uploaded"
    
    photo_preview.short_description = 'Photo Preview'