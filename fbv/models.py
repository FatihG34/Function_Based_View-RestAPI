from django.db import models

# Create your models here.
class Countries(models.Model):
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name
    


class People(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    country = models.ForeignKey(Countries,related_name="countries", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_mame} {self.last_name}"