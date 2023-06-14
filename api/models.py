from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Posts(models.Model):
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to="image",null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    comment=models.CharField(max_length=300)
    post_name=models.ForeignKey(Posts,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class UserProfile(models.Model):
    is_active=models.BooleanField(default=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to="images",null=True)
    bio=models.CharField(max_length=500)
    time_line_pic=models.ImageField(upload_to="images",null=True)