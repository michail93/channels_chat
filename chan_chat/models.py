from django.db import models

# Create your models here.


class Post(models.Model):
    text = models.CharField(max_length=250)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"post - {self.pub_date}"
