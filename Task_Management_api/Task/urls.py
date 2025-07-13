from django.urls import path, include
from .views import TaskViewsSet, ProjectViewsSet, UserViewsSet, TaskAssignmentViewsSet, ReminderViewsSet
from rest_framework.routers import DefaultRouter    

router = DefaultRouter()
router.register(r'tasks', TaskViewsSet)
router.register(r'projects', ProjectViewsSet)
router.register(r'users', UserViewsSet)
router.register(r'taskassignments', TaskAssignmentViewsSet)
router.register(r'reminders', ReminderViewsSet)

urlpatterns = [
    path('', include(router.urls)),
]