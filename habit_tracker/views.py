# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet

from habit_tracker.models import HabitModel, RewordModel
from habit_tracker.serializers import HabitModelSerializer, RewordModelSerializer

from rest_framework.response import Response




import logging

from habit_tracker.validators import check_reword, is_pleasant_validator

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
        habit_id = int(self.kwargs.get('pk'))
        logger.info(f'id привычки: {habit_id}')
        data = self.request.data
        pleasant_hab = data.get('pleasant_hab', False)
        reword = data.get('reword', False)
        is_pleasant_validator(pleasant_hab)
        check_reword(pleasant_hab, reword, habit_id)
        serializer.save()



class RewordViewSet(ModelViewSet):
    '''ViewSet для операций над model: habit_tracker.RewordModel.'''


    queryset = RewordModel.objects.all()
    serializer_class = RewordModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




