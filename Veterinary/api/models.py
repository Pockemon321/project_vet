from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')

    def __str__ (self):
        return f'{self.title}'

    class Meta:
        ordering = ['title']
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Orders(models.Model):
    date_of_order = models.DateTimeField()
    categories = models.ForeignKey('Categories', related_name='orders_categories', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=60, blank=False, default='')
    age = models.IntegerField(default=0)
    description = models.TextField(max_length=200, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='orders_user', on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_of_order']
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
