from django.db import models


class Statistic(models.Model):
    date = models.DateField(verbose_name='Дата события')
    views = models.PositiveIntegerField(verbose_name='Кол-во показов')
    clicks = models.PositiveIntegerField(verbose_name='Кол-во кликов')
    cost = models.FloatField(verbose_name='Стоимость кликов в рублях')

    def __str__(self):
        return f'Статистика за {self.date}'

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'
        ordering = ['date']

    def get_cpc(self):
        return self.cost / self.clicks

    def get_cpm(self):
        return (self.cost / self.views) * 1000
