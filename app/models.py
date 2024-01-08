from django.db import models

# Create your models here.
class EmployeeInfo(models.Model):
    Name = models.CharField(max_length = 100, primary_key = True)
    Experience = models.IntegerField()
    Mobile = models.IntegerField(unique = True)
    Email = models.EmailField()
    Portfolio = models.URLField()

    def __str__(self):
        return self.Name


class Show_Info(models.Model):
    Name = models.ForeignKey(EmployeeInfo, on_delete = models.CASCADE)
    

    def __str__(self):
        return self.Name
