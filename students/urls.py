from django.urls import path, include
from .views import home, class_list, student_list, student_detail, notifications, assignments, about, class_timetable

urlpatterns = [
    path('', home, name='home'),  # Home Page
    path('notifications/', notifications, name='notifications'),
    path('assignments/', assignments, name='assignments'),
    path('about/', about, name='about'),
    path('classes/', class_list, name='class_list'),  # Class List Page
    path('<int:class_id>/', student_list, name='student_list'),  # Student List Page
    path('student/<int:student_id>/', student_detail, name='student_detail'),
    path('<int:class_id>/timetable/', class_timetable, name='class_timetable'),
    path("chat/", include("chat.urls")),
]