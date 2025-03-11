from django.contrib import admin
from .models import Student, Classroom, Timetable

class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'classroom')
    search_fields = ('name', 'roll_no')  # Allows searching by name and roll number
    list_filter = ('classroom',)  # Filter students by classroom

class TimetableAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'day', 'subject', 'start_time', 'end_time', 'teacher')
    list_filter = ('classroom', 'day')  # Filter by classroom and day
    search_fields = ('subject', 'teacher')  # Search by subject and teacher name
    ordering = ('classroom', 'day', 'start_time')  # Order by class, day, and time

admin.site.register(Student, StudentAdmin)
admin.site.register(Classroom)
admin.site.register(Timetable, TimetableAdmin)  # Register Timetable model
