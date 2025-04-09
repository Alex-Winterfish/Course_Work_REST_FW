# -*- coding: utf-8 -*-
from django.db import models

class HabitModel(models.Model):
    '''Модель привычки model: habit_tracker.models.HabitModel.'''
    name = models.TimeField(max_length=200, verbose_name='Название привычки')
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, verbose_name='Автор привички', related_name='user')
    location = models.CharField(max_length=400, verbose_name='место выполнеия привычки')
    perform_time = models.TimeField(verbose_name='когда выполнять привичку')
    substance = models.CharField(max_length=2000, verbose_name='содержание привычки')
    is_pleasant = models.BooleanField(verbose_name='признак приятной привычки')
    period = models.DateField(verbose_name='периодичность выполнения')
    reword = models.ManyToManyField('habit_tracker.RewordModel', verbose_name='вознаграждение')
    lasting_time = models.TimeField(verbose_name='длительность выполнения',)

    def __str__(self):
        if self.is_pleasant:
            return f'Привычка {self.name}'
        else:
            return f'Привычка {self.name}, не реже одного раза в {self.period}.'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'


class RewordModel(models.Model):
    '''Модель вознаграждения model: habit_tracker.models.RewordModel.'''
    name = models.CharField(max_length=200, verbose_name='название вознаграждения')
    description = models.CharField(max_length=1000, verbose_name='описнаие вознаграждения')
    habit = models.ManyToManyField('habit_tracker.HabitModel', verbose_name='')

    def __str__(self):
        return f'Вознаграждение {self.name}'
    class Meta:
        verbose_name = 'Вознаграждение'
        verbose_name_plural = 'Вознаграждения'
