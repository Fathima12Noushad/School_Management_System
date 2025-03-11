from django.db import models

class Classroom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()  # No unique=True
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('roll_no', 'classroom')  # Ensure roll_no is unique within a classroom

    def __str__(self):
        return f"{self.roll_no} - {self.name} ({self.classroom.name})"

class Timetable(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)  # e.g., Monday, Tuesday, etc.
    subject = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.classroom.name} - {self.day} - {self.subject}"