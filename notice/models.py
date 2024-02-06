from django.db import models

from users.models import User

"Модель для обьявлений"


class Notice(models.Model):
    title = models.CharField(max_length=40, verbose_name='название товара')
    price = models.IntegerField(verbose_name='цена')
    description = models.CharField(max_length=150, verbose_name='описание товара')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='автор',
                               related_name='author_notice')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
