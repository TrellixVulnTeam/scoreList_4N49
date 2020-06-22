from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

# 客户端分数表
class Client(models.Model):
    client_num =models.CharField(max_length=50)
    score = models.IntegerField(verbose_name='分数', default=0,
                                validators=[MaxValueValidator(10000000), MinValueValidator(1)])


    class Meta:
        verbose_name = '分数表'
        verbose_name_plural = verbose_name

# 名次表
class Rank(models.Model):
    c_id = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)
    rank = models.IntegerField(verbose_name='名次', validators=[MinValueValidator(1)])
