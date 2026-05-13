from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    college = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.name