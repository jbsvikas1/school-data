from django.db import models

# Create your models here.
class classdetails(models.Model):
    name = models.CharField(max_length=30)
    teacher_name = models.CharField(max_length=30)
    student_count = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class student(models.Model):
    stdname = models.CharField(max_length=100)
    stdage = models.IntegerField()
    stdclass = models.ForeignKey(classdetails,null=True, on_delete=models.DO_NOTHING)
    stdmail = models.EmailField()

    def __str__(self):
        return self.stdname