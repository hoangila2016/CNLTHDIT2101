from django.contrib import admin
from .models import Category,Course,Tag,Lesson
from django.utils.html import mark_safe
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_filter= ['id','name']
    search_fields =['name']

class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ['img']

    def img(self, course):
        if course:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=course.image.name)
            )

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }




admin.site.register(Category,CategoryAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Tag)
admin.site.register(Lesson)

