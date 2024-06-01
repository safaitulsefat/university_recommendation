from django.db import models

class University(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'CSE'),
        ('EEE', 'EEE'),
    ]
    
    university = models.CharField(max_length=100)
    rank = models.IntegerField()
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)
    cost = models.IntegerField()
    credit = models.IntegerField()
    weiver = models.BooleanField()
    admission_fee = models.IntegerField()
    minimum_gpa = models.FloatField()
    hostel = models.BooleanField()
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.university
