from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from habit_tracker.models import HabitModel, RewordModel
from habit_tracker.serializers import HabitModelSerializer, RewordModelSerializer


class HabitViewSet(ModelViewSet):
    '''ViewSet для операций над model: habit_tracker.HabitModel.'''

    queryset = HabitModel.objects.all()
    serializer_class = HabitModelSerializer
    #добавить права допуска

class RewordViewSet(ModelViewSet):
    '''ViewSet для операций над model: habit_tracker.RewordModel.'''


    queryset = RewordModel.objects.all()
    serializer_class = RewordModelSerializer





