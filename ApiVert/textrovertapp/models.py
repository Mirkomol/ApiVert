from django.db import models



class TextroVertAppData(models.Model):
    name = models.CharField(max_length=200)
    data = models.TextField()
    category = models.CharField(max_length=200, default='noemotion')


    def __str__(self):
        return self.name


