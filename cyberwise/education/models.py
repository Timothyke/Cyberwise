from django.db import models

# Create your models here.
class Module(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    quiz = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
