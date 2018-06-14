import os
import time

from django.db import models
from django.contrib.auth.models import User

def todo_attach_path(instance, filename):
    return os.path.join('todo',str(time.time()),filename)

class Tag(models.Model):
    title = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.title

# Create your models here.
class Todo(models.Model):
    title = models.CharField('標題', max_length = 255)
    content = models.TextField('內容', max_length = 500)
    status = models.BooleanField('已完成',default = False)
    tags = models.ManyToManyField(Tag, verbose_name = '標籤')
    creator = models.ForeignKey(User,on_delete = models.PROTECT, verbose_name = '建立者')
    attach = models.FileField('附件', blank = True, upload_to=todo_attach_path)

    def __str__(self):
        return self.title