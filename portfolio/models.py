from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title