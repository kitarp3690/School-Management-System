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

#Session_Year to Batch (website ma session word use garna paideina!!!!)
class Batch(models.Model):
    batch_start=models.CharField(max_length=100)
    batch_end=models.CharField(max_length=100)
    
    def __str__(self):
        return self.batch_start + " To " + self.batch_end

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
    rollno = models.CharField(max_length=20, unique=True, null=True, blank=True)  
    course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING,default=1)
    batch_id=models.ForeignKey(Batch,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.admin.first_name} {self.admin.last_name}"

    # def __str__(self):
    #     return self.admin.first_name + " " + self.admin.last_name
    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    admin =models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    gender=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # subject_id=models.ForeignKey(Subject,on_delete=models.DO_NOTHING,default=6)
    subjects = models.ManyToManyField(Subject, related_name="staff_members")

    def __str__(self):
        return self.admin.username

class Attendance(models.Model):
    subject_id=models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    attendance_date=models.DateField()
    batch_year_id=models.ForeignKey(Batch,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject_id.name
    
class Attendance_Report(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendance_id= models.ForeignKey(Attendance,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student_id.admin.first_name
    
class Staff_Notification(models.Model):
    staff_id =  models.ForeignKey(Staff,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.staff_id.admin.first_name
    
class Student_Notification(models.Model):
    student_id =  models.ForeignKey(Student,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.student_id.admin.first_name

class Staff_Leave(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default= 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name

class Student_Leave(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default= 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.student_id.admin.first_name + self.student_id.admin.last_name

class StudentResult(models.Model): 
    student_id = models.ForeignKey (Student,on_delete=models.CASCADE) 
    subject_id = models.ForeignKey (Subject,on_delete=models.CASCADE)
    internal_mark = models. IntegerField() 
    exam_mark = models. IntegerField() 
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.student_id.admin.first_name
