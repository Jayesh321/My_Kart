from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()

    class meta():
        db_table="Registration"

    def __str__(self):
        return self.username
