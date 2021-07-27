from django.db import models

# Create your models here.
class irisdata(models.Model):
    id = models.AutoField(primary_key=True)
    Sepallength = models.FloatField()
    Sepalwidth = models.FloatField()
    Petallength = models.FloatField()
    Petalwidth = models.FloatField()
    Irispred = models.CharField(max_length=30)

    def __str__(self):
        return self.Irispred