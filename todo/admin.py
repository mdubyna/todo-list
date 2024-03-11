from django.contrib import admin
from django.contrib.auth.models import Group

from todo.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("created_at", "deadline", "done")
    list_filter = ("tags", "done", "created_at")
    search_fields = ("tags", )


admin.site.register(Tag)

admin.site.unregister(Group)
