from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, null=True)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to="post/%Y/%m/%d", null=True)

    def __str__(self):
        return self.description