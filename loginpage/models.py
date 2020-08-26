from django.db import models
from django.contrib.auth.models import  User

# Create your models here.
class Login_page(models.Model):
    Profile_pic = models.ImageField(upload_to='Profile_pic', blank=True)
    url = models.URLField(blank=True)
    # bio = models.CharField(max_length=300, blank=True)
    # something_about_yourself = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return self.Profile_pic or self.url
    # def __str__(self):
    #     return self.url
