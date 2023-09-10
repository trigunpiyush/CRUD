from django.contrib.auth.models import User
from django.db import models

class CuboidBox(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)  
    length = models.DecimalField(max_digits=10, decimal_places=2)  
    breadth = models.DecimalField(max_digits=10, decimal_places=2)  
    height = models.DecimalField(max_digits=10, decimal_places=2)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Box #{self.id} - {self.creator.username}"
    
    def area(self):
        return self.length * self.breadth

    def volume(self):
        return self.length * self.breadth * self.height
