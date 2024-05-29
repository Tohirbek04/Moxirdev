from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.models import Course
from apps.permissions import IsOwner
from apps.serializers import CourseListSerializers, CourseRetrieveSerializers


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializers
    permission_classes = AllowAny,


class CourseRetrieveAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetrieveSerializers
    permission_classes = IsOwner,

