# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):
    help = "Create schedule for a task"

    def handle(self, *args, **options):

        new_schedule = {"every": 600, "period": IntervalSchedule.SECONDS}

        schedule, created = IntervalSchedule.objects.get_or_create(**new_schedule)

        new_task = {
            "interval": schedule,
            "name": "user_deactivate",
            "task": "habit_tracker.tasks.reminder_task",
        }

        PeriodicTask.objects.create(**new_task)

        self.stdout.write(self.style.SUCCESS("Successfully set the schedule"))