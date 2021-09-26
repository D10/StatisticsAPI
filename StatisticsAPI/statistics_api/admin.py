from django.contrib import admin

from .models import Statistic


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    model = Statistic
    list_display = ('id', 'date', 'views', 'clicks', 'cost')
