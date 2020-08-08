from django.db import models

# Create your models here.


class Company(models.Model):
    client_name = models.CharField(max_length=100)
    created_at =models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)



    def __str__(self):
        return self.client_name