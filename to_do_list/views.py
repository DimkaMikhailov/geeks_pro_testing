from rest_framework.viewsets import ModelViewSet
from to_do_list.models import Task
from to_do_list.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'
