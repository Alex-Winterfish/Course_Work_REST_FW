# -*- coding: utf-8 -*-
from rest_framework import serializers

from habit_tracker.models import HabitModel, RewordModel

class HabitModelSerializer(serializers.ModelSerializer):
    '''Сериалайзер model: habit_tracker.models.HabitModel.'''

    class Meta:
        model = HabitModel
        fields = '__all__'


class RewordModelSerializer(serializers.ModelSerializer):
    '''Сериалайзер model: habit_tracker.models.RewordModel.'''

    class Meta:
        model = RewordModel
        fields = '__all__'