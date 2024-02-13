from rest_framework.routers import DefaultRouter

from task.api.task_views import TaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')


urlpatterns = router.urls