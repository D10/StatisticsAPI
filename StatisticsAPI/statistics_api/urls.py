from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import StatisticViewSet

statistic_view = StatisticViewSet.as_view({
    'get': 'get_statistics',
    'post': 'create',
    'delete': 'clear_statistics'
})


urlpatterns = format_suffix_patterns([
    path('statistics/', statistic_view)
])
