from django.contrib import admin
from .models import *

class GroupAdmin(admin.ModelAdmin):
    list_display =('name', 'period_price', 'schedule')
    list_display_links = ('name',)
    search_fields = ('name',)
    # list_editable =
    # list_filter =
    # prepopulated_fields =
class ClubCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount')
    list_display_links = ('name',)
    def save_model(self, request, obj, form, change):
        existing_objects = ClubCard.objects.filter(name=obj.name)
        if existing_objects.exists():
            return
        super().save_model(request, obj, form, change)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'card')
    list_display_links = ('name',)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'start_time', 'end_time', 'lesson_price')
    list_display_links = ('subject_name',)
    def save_related(self, request, form, formsets, change):
        instance = form.instance
        if instance.start_time > instance.end_time:
            return
        super().save_related(request, form, formsets, change)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('username', 'subject_name')
    list_display_links = ('username',)
class DayAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    def save_model(self, request, obj, form, change):
        existing_objects = Day.objects.filter(name=obj.name)
        if existing_objects.exists():
            return
        super().save_model(request, obj, form, change)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('weeks_count',)
class ClubGymAdmin(admin.ModelAdmin):
    list_display = ('name',)
    def save_model(self, request, obj, form, change):
        existing_objects = ClubGym.objects.filter(name=obj.name)
        if existing_objects.exists():
            return
        super().save_model(request, obj, form, change)

admin.site.register(Group, GroupAdmin)
admin.site.register(ClubCard, ClubCardAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Master, MasterAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(ClubGym, ClubGymAdmin)