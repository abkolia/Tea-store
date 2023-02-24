from django.db import models

class Articles(models.Model):
    title = models.CharField('Название товара', max_length=50)
    desc = models.CharField('Описание', max_length=250)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'