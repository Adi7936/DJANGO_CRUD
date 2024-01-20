from django.db import models

# Create your models here.
#Section Model
class Section(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



#Student Model
class Student(models.Model):
    name = models.CharField(max_length=255)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='students')

    def __str__(self) -> str:
        return self.name