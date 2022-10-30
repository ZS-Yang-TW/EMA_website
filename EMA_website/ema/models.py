from tabnanny import verbose
from django.db import models

# Create your models here.

class TB_1(models.Model):
    name = models.CharField(max_length = 10)
    question = models.CharField(max_length = 10)
    _time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-_time']
        verbose_name = "問題歷史記錄"
        verbose_name_plural = "問題歷史紀錄"
