from django.db import models

# Create your models here.
from django.db import models

class App(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='apps/')
    download_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title