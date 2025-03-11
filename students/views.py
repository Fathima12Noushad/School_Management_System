# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Student, Classroom, Timetable
from collections import defaultdict

def class_list(request):
    classes = Classroom.objects.all()  # Fetch all classrooms
    return render(request, 'students/class_list.html', {'classes': classes})

def student_list(request, class_id):
    classroom = get_object_or_404(Classroom, id=class_id)
    students = Student.objects.filter(classroom=classroom)  # Fetch students from the selected class
    return render(request, 'students/student_list.html', {'students': students, 'classroom': classroom})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_detail.html', {'student': student})

def home(request):
    return render(request, 'students/home.html')

def notifications(request):
    return render(request, 'students/notifications.html')

def assignments(request):
    return render(request, 'students/assignments.html')

def about(request):
    return render(request, 'students/about.html')

def class_timetable(request, class_id):
    classroom = get_object_or_404(Classroom, id=class_id)
    timetable_entries = Timetable.objects.filter(classroom=classroom).order_by('day', 'start_time')

    # Group timetable by day
    grouped_timetable = defaultdict(list)
    for entry in timetable_entries:
        grouped_timetable[entry.day].append(entry)

    return render(request, 'students/class_timetable.html', {
        'classroom': classroom,
        'grouped_timetable': dict(grouped_timetable)
    })