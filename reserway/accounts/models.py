from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookingAgent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='booking_agent')
    address=models.TextField(max_length=500,blank=False)

    def __str__(self):
        return str(self.user.id)+"  "+self.user.first_name+" "+self.user.last_name

