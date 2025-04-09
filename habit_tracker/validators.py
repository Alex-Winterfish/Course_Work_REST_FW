from rest_framework.serializers import ValidationError

class ExcludeRewordValidator:
    '''Валидатор для исключения одновоеменного
    выбора приятной привычки и вознаграждения'''

    def __init__(self, field_pls, field_rew):
        self.field_pls = field_pls
        self.field_rew = field_rew

    def __call__(self, value):
        field_pls = dict(value).get(self.field_pls, False)
        field_raw = dict(value).get(self.field_rew, False)
        if field_raw and field_pls:
            raise ValidationError(
                detail='Нельзя одновременно делать привычку приятной и утанавливать за нее вознаграждение'
            )


class PerformTimeValidator:
    '''Валидатор для проверки времы выполения привычки.
    Не должно быть больше 120 сек.'''
    pass

class IsPleasantValidator:
    '''Валидатор для провреки связанной model: habit_tracker.HabitModel.
    Параметр модели is_pleasant должен быть True.'''
    pass

class PeriodValidator:
    '''Валидатор для проверки периода выполения привычки.
    Не дожен быть реже раза в неделю'''
    pass