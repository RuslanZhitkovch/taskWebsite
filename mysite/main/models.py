from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Название', max_length=50,null = False)
    task = models.TextField('Описание',null = True)
    published = models.DateTimeField('Время публикации',auto_now_add=True,db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'