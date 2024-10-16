from django.db import models

class Pets(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pests/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} from {self.location}"
