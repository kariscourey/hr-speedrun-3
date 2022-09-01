from django.db import models

class MyApps(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField(auto_now=False)

    def __str__(self):
        return self.name
