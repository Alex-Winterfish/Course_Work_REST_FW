# -*- coding: utf-8 -*-
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habit_tracker.models import HabitModel, RewordModel
from habit_tracker.serializers import HabitModelSerializer, RewordModelSerializer





import logging

from habit_tracker.validators import check_reword, is_pleasant_validator
from users.permissions import IsOwnerPermission, IsPublicPermission

logger = logging.getLogger(__name__)

class HabitViewSet(ModelViewSet):
    '''ViewSet для операций над model: habit_tracker.HabitModel.'''
    queryset = HabitModel.objects.all()
    serializer_class = HabitModelSerializer

    def get_queryset(self):
        user = self.request.user
        return HabitModel.objects.filter(is_public=True) | HabitModel.objects.filter(user=user)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        logger.info(f'Данные для обновления: {self.request.data}')
        habit_id = int(self.kwargs.get('pk'))
        logger.info(f'id привычки: {habit_id}')
        data = self.request.data
        pleasant_hab = data.get('pleasant_hab', False)
        reword = data.get('reword', False)
        is_pleasant_validator(pleasant_hab) #проводим валидацию что привычка не является приятной
        check_reword(pleasant_hab, reword, habit_id) #проводим валидацию что в изменяемой модели нет связанный вознаграждений и приятных привычек
        serializer.save()

    def get_permissions(self):

        if self.action == 'create':
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = (IsOwnerPermission,)
        elif self.action == 'retrieve':
            self.permission_classes = (IsOwnerPermission, IsPublicPermission)
        elif self.action == 'list':
            self.permission_classes = (IsOwnerPermission, IsPublicPermission,)

        return super().get_permissions()


class RewordViewSet(ModelViewSet):
    '''ViewSet для операций над model: habit_tracker.RewordModel.'''


    queryset = RewordModel.objects.all()
    serializer_class = RewordModelSerializer
    permission_classes = (IsOwnerPermission, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()




