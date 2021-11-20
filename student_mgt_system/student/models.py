from django.db import models

# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=20)
    standard = models.CharField(max_length=20)

    def __str__(self):
        return str(self.first_name) + ' ' + (self.last_name)


    