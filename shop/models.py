from django.db import models

# Create your models here.
class shop(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)



class Registration(models.Model):
    student = models.OneToOneField('Student', models.DO_NOTHING, primary_key=True)  # The composite primary key (student_id, webinar_id) found, that is not supported. The first column is selected.
    webinar = models.ForeignKey('Webinar', models.DO_NOTHING)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registration'
        unique_together = (('student', 'webinar'),)


class Student(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    mentor = models.ForeignKey('Teacher', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Teacher(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher'


class Webinar(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, models.DO_NOTHING, blank=True, null=True)
    visibility = models.TextField()  # This field type is a guess.
    starts_on = models.DateTimeField(blank=True, null=True)
    ends_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webinar'
