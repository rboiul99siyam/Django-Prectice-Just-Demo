from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    father_name = models.TextField()
    address = models.TextField()
    def __str__(self) -> str:
        return f'Name : {self.name} - Roll : {self.roll} FatherName : {self.father_name} address : {self.address}'
    