from django.db import models



class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=20)
    esal = models.IntegerField()
    choice = [('WFH', 'Work From Home'), ('WFO', 'Work From Office')]
    mode = models.CharField(max_length=10, choices=choice)
