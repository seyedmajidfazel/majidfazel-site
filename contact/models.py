from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contactclass(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    subject = models.CharField(max_length=80)
    message = models.TextField()

    def __str__(self):
        return str(self.user) + ': ' + str(self.subject)