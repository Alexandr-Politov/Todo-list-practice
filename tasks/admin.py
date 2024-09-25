from django.contrib import admin

from tasks.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "deadline", "is_done"]
    search_fields = ["name"]
    list_filter = ["deadline", "is_done"]

admin.site.register(Tag)
