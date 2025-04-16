# -*- coding: utf-8 -*-
from rest_framework import serializers

from habit_tracker.models import HabitModel, RewordModel
from habit_tracker.validators import ExcludeRewordValidator, PeriodValidator


class HabitModelSerializer(serializers.ModelSerializer):
    '''Сериалайзер model: habit_tracker.models.HabitModel.'''

    class Meta:
        model = HabitModel
        fields = '__all__'
        validators = [ExcludeRewordValidator(field_pls='pleasant_hab', field_rew='reword'),
                      PeriodValidator(field_period='period', field_last_time='lasting_time')]


class RewordModelSerializer(serializers.ModelSerializer):
    '''Сериалайзер model: habit_tracker.models.RewordModel.'''

    class Meta:
        model = RewordModel
        fields = '__all__'