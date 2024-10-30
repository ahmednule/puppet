from django.db import models

class Pets(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    age=models.IntegerField(default=0, null=False)
    contact=models.IntegerField(default='0706703863',null=False)
    likes=models.CharField(max_length=20, blank=True, null=False)
    dislikes=models.CharField(max_length=20, blank=True, null=False)
    image = models.ImageField(upload_to='pests/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} from {self.location}"
