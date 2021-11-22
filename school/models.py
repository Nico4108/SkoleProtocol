from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    adress = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
      return "{}".format(self.name)
    
    class Meta:
        db_table = 'School'