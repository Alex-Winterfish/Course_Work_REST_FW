# Трекер Привычек.

1. Запуск:
 необходимые переменные окружения указаны в файле .env.sample

Выполнить команду:
```commandline
docker-compose up --build -d
```
Выполнится запуск контейнеров, запонится база данных и добавится периодическая задача

2. Проверка работоспособности контейнеров.

2.1. База данных.

Выполнить команду:

```commandline
docker-compose exac db psql -U postgres -d [POSTGRES_DB] -h db -p 5432
```
POSTGRES_DB - название базы данных из переменных окружения

Выполнить запрос к базе данных \d

Будет получена таблица 
```
 Schema |                    Name                    |   Type   |  Owner
--------+--------------------------------------------+----------+----------
 public | auth_group                                 | table    | postgres
 public | auth_group_id_seq                          | sequence | postgres
 public | auth_group_permissions                     | table    | postgres
 public | auth_group_permissions_id_seq              | sequence | postgres
 public | auth_permission                            | table    | postgres
 public | auth_permission_id_seq                     | sequence | postgres
 public | django_admin_log                           | table    | postgres
 public | django_admin_log_id_seq                    | sequence | postgres
 public | django_celery_beat_clockedschedule         | table    | postgres
 public | django_celery_beat_clockedschedule_id_seq  | sequence | postgres
 public | django_celery_beat_crontabschedule         | table    | postgres
 public | django_celery_beat_crontabschedule_id_seq  | sequence | postgres
 public | django_celery_beat_intervalschedule        | table    | postgres
 public | django_celery_beat_intervalschedule_id_seq | sequence | postgres
 public | django_celery_beat_periodictask            | table    | postgres
 public | django_celery_beat_periodictask_id_seq     | sequence | postgres
 public | django_celery_beat_periodictasks           | table    | postgres
 public | django_celery_beat_solarschedule           | table    | postgres
 public | django_celery_beat_solarschedule_id_seq    | sequence | postgres
 public | django_content_type                        | table    | postgres
 public | django_content_type_id_seq                 | sequence | postgres
 public | django_migrations                          | table    | postgres
 public | django_migrations_id_seq                   | sequence | postgres
 public | django_session                             | table    | postgres
 public | habit_tracker_habitmodel                   | table    | postgres
 public | habit_tracker_habitmodel_id_seq            | sequence | postgres
 public | habit_tracker_rewordmodel                  | table    | postgres
 public | habit_tracker_rewordmodel_id_seq           | sequence | postgres
 public | users_customuser                           | table    | postgres
 public | users_customuser_groups                    | table    | postgres
 public | users_customuser_groups_id_seq             | sequence | postgres
 public | users_customuser_id_seq                    | sequence | postgres
 public | users_customuser_user_permissions          | table    | postgres
 public | users_customuser_user_permissions_id_seq   | sequence | postgres
(34 rows)
```
2.2. Celery.

Выполнить команду
```commandline
docker-compose exec celery python manage.py shell -c "from habit_tracker.tasks import control_task; control_task.delay()"
```
Посмотреть логи celery
```commandline
docker-compose logs celery
```
В логах должна появиться следующая запись:
celery-1  | [2025-05-05 18:17:36,455: INFO/ForkPoolWorker-7] Task habit_tracker.tasks.control_task[bae027de-f1ac-4404-aacf-bd00b766018a] succeeded in 0.002770500001133769s: 'celary
 is working!'

2.3. Сервис habit_tracker.

выполнить команду
```commandline
docker-compose exec habit_tracker coverage run manage.py tes
```
Запустится тестирование приложения. Посмотреть покрытие тестами, выполнить команду:

```commandline
docker-compose exec habit_tracker coverage report 
```
