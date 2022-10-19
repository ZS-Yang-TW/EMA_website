from email.policy import default
from secrets import choice
from django.db import models

class TB_1(models.Model):
    
    name = models.CharField(max_length = 64)
    age = models.IntegerField()
    
    MY_CHOICES = [
        ('0','加法'),
        ('1','減法'),
        ('2','乘法'),
        ('3','除法'),
    ]
    
    type = models.CharField(
            max_length = 1, 
            choices = MY_CHOICES,
            default = '0',
        )
    
    # 資料庫創立時間
    _time = models.DateTimeField(auto_now_add = True)
    
    
    
    # Data name setting
    def __str__(self):
        return self.name
    
    # Datadase Setting
    class Meta:
        ordering = ['-_time'] # The newest data at the top.
        verbose_name = "用戶資料庫"
        verbose_name_plural = "用戶資料庫"