
from django.db import models

from users.models import User

from notice.models import Notice




class Fidback(models.Model):

    text = models.CharField(max_length=150, verbose_name='текст')
    ad = models.ForeignKey(Notice, on_delete=models.CASCADE, verbose_name='номер обьявления')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='автор', related_name='author_fidback')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='время создания')

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
