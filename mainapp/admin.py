from django.contrib import admin
from mainapp import models as mainapp_models
from django.utils.translation import gettext_lazy as _


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'preambule', 'deleted', 'created']
    ordering = ['-id', 'title']
    list_per_page = 4 
    list_filter = ['deleted', 'body_as_markdown']
    search_fields = ['body']
    actions = ['mark_deleted']

@admin.register(mainapp_models.Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'cost', 'deleted'] 
    ordering = ['-name', 'description'] 
    list_per_page = 4
    list_filter = ['deleted','description_as_markdown'] 
    search_fields = ['description', 'name']
    actions = ['mark_deleted']