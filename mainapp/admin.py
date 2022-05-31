from django.contrib import admin
from mainapp import models as mainapp_models
from django.utils.translation import gettext_lazy as _


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'preambule', 'deleted', 'created']
    ordering = ['-id', 'title']
    list_per_page = 4 
    list_filter = ['deleted', 'body_as_markdown']
    search_fields = ["title", "preambule", "body"]
    actions = ['mark_deleted']

@admin.register(mainapp_models.Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'cost', 'deleted'] 
    ordering = ['-name', 'description'] 
    list_per_page = 4
    list_filter = ['deleted','description_as_markdown'] 
    search_fields = ['description', 'name']
    actions = ['mark_deleted']

@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "num", "title", "deleted"]
    ordering = ["-course__name", "-num"]
    list_per_page = 5
    list_filter = ["course", "created", "deleted"]
    actions = ["mark_deleted"]

    def get_course_name(self, obj):
        return obj.course.name

    get_course_name.short_description = _("Course")
    
    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")