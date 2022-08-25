from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class bill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default="")
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
        
class payee(models.Model):
    billId = models.ForeignKey(bill,on_delete=models.CASCADE,related_name='persons')
    name = models.CharField(max_length=50)
    pay = models.IntegerField()