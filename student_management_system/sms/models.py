from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_CHOICES = (
        (1, 'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT'),
    )
    user_type = models.CharField(choices=USER_CHOICES, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

    def __str__(self):
        return self.email

class Session_Year(models.Model):
    session_start=models.CharField(max_length=100)
    session_end=models.CharField(max_length=100)
    
    def __str__(self):
        return self.session_start + " To " + self.session_end

class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    admin =models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    gender=models.CharField(max_length=100)
    course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING,default=1)
    session_year_id=models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    
class Staff(models.Model):
    admin =models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    gender=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username
    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Attendence(models.Model):
    subject_id=models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    attendence_date=models.DateField()
    Session_Year_id=models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject_id.name
    
class Attendence_Report(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendence_id= models.ForeignKey(Attendence,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student_id.admin.first_name
    

