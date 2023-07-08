from django.db import models
from django.contrib.auth.models import User, Group

class Mainmenu(models.Model):
    menucode = models.ImageField()
    menuname = models.CharField(max_length=100)
    menutype = models.ImageField()

    def __str__(self):
        return self.menuname

    objects = models.Manager()


class MenuList(models.Model):
    menucode = models.ImageField()
    menuname = models.CharField(max_length=100)
    menutype = models.ImageField()
    submenuname = models.CharField(max_length=100)
    menulink = models.CharField(max_length=100)
    
    def __str__(self):
        return self.menuname
    
    objects = models.Manager()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
