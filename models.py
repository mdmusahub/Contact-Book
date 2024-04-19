from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    C_id = models.IntegerField(primary_key=True)
    C_name = models.CharField(max_length=255)
    C_number = models.IntegerField()
    C_email =  models.EmailField(max_length=50)
    C_address = models.TextField()

