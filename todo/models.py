from django.db import models

# Create your models here.
# model in django is inherited from the models.model each models refer to the table in database 
class todo(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField()

    def __str__(self):
        return self.name
