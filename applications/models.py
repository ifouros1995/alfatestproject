from django.db import models


class Application(models.Model):

    protocol_number = models.IntegerField()
    name = models.CharField(max_length=264,unique=True)
    address = models.CharField(max_length=264,unique=True)
    date = models.DateField(auto_now=True)


    def __str__(self):
        return self.name
