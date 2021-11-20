from django.db import models

# Create your models here.

class teacher(models.Model):
    teacher_first_name = models.CharField(max_length=20)
    teacher_last_name = models.CharField(max_length=20)
    teacher_mobile_no = models.IntegerField()
    teacher_address = models.CharField(max_length=20)
    teacher_education = models.CharField(max_length=20)
    teacher_allocated_class = models.CharField(max_length=20)

    
    def __str__(self):
        # return self.teacher_first_name and self.teacher_last_name
        return str(self.teacher_first_name) + ' ' + (self.teacher_last_name)