# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet

from habit_tracker.models import HabitModel, RewordModel
from habit_tracker.serializers import HabitModelSerializer, RewordModelSerializer

from rest_framework.response import Response




import logging

logger = logging.getLogger(__name__)

class HabitViewSet(ModelViewSet):
    '''ViewSet для операций над model: habit_tracker.HabitModel.'''

    queryset = HabitModel.objects.all()
    serializer_class = HabitModelSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    #добавить права допуска

    def perform_update(self, serializer):
        logger.info(f'Данные для обновления: {self.request.data}')
        logger.info(f'Валидированные данные: {serializer.validated_data}')
        super().perform_update(serializer)



class RewordViewSet(ModelViewSet):
    '''ViewSet для операций над model: habit_tracker.RewordModel.'''


    queryset = RewordModel.objects.all()
    serializer_class = RewordModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




