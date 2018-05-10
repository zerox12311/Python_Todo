from django.contrib import admin

from .models import Todo, Tag

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','creator','status')
    list_filter = ('status',)
    search_fields = ('title','creator__username')



admin.site.register(Todo,TodoAdmin)
admin.site.register(Tag)
