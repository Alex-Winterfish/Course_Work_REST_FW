from rest_framework.routers import SimpleRouter
from habit_tracker.apps import HabitTrackerConfig

from habit_tracker.views import HabitViewSet, RewordViewSet

app_name = HabitTrackerConfig.name

router = SimpleRouter()
router.register('habits', HabitViewSet)
router.register('rewords', RewordViewSet)

urlpatterns = router.urls