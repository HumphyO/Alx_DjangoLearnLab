from rest_framework import viewsets
from .models import Task, Project, User, TaskAssignment, Reminder
from .serializers import TaskSerializer, ProjectSerializer, UserSerializer, TaskAssignmentSerializer, ReminderSerializer
# Create your views here.

class TaskViewsSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ProjectViewsSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class UserViewsSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskAssignmentViewsSet(viewsets.ModelViewSet):
    queryset = TaskAssignment.objects.all()
    serializer_class = TaskAssignmentSerializer

class ReminderViewsSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer   

