import email
from operator import mod
from unicodedata import name
from django.db import models

#email name pwd _time

class User(models.Model):
    email = models.EmailField(unique=True) # unique: 保證 Email 的唯一性
    name = models.CharField(max_length = 64)
    pwd = models.CharField(max_length = 64)
    question = models.CharField(max_length = 64)
    _time = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-_time']
        verbose_name = '用戶資料庫'
        verbose_name_plural = '用戶資料庫'
        
        
        
        
        
