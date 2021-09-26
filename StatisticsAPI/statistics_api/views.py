import logging
import datetime

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Statistic
from .serializers import StatisticSerializer

logger = logging.getLogger('mailings')


class StatisticViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, ]
    serializer_class = StatisticSerializer
    queryset = Statistic.objects.all()

    def to_datetime(self, date):
        return datetime.datetime.strptime(date, '%Y-%m-%d')

    def get_dates(self):
        """Получаем даты из тела запроса и проводим их валидацию"""
        from_date = self.request.POST.get('from')
        to_date = self.request.POST.get('to')
        if self.to_datetime(from_date) > self.to_datetime(to_date):
            return
        return from_date, to_date

    @action(detail=False)
    def get_statistics(self, *args, **kwargs):
        """Отдает в качестве ответа статистику за определенный промежуток времени отсортированную по дате"""
        from_date, to_date = self.get_dates()
        logger.info(f'GET statistics FROM {from_date} TO {to_date}') # Отправляем в логи сообщение о GET запросе
        query = Statistic.objects.filter(date__gt=from_date).filter(date__lt=to_date).order_by('date')
        response = StatisticSerializer(query, many=True)
        return Response(response.data)

    @action(detail=False)
    def clear_statistics(self, *args, **kwargs):
        """Удаляет всю статистику из базы"""
        logger.info(f'DROP ALL STATISTICS')
        Statistic.objects.all().delete()
        return Response({'success': True})
