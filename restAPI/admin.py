from django.contrib import admin

# Register your models here.
from restAPI.models import Task

@admin.register(Task)
class TaskAdminView(admin.ModelAdmin):
    list_display= ('title','description', 'status')
