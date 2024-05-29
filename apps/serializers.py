from rest_framework.serializers import ModelSerializer

from apps.models import Course, Category, CourseVideo


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseListSerializers(ModelSerializer):
    category = CategorySerializers(read_only=True)

    class Meta:
        model = Course
        fields = 'title', 'category'


class CourseVideoSerializers(ModelSerializer):
    class Meta:
        model = CourseVideo
        fields = '__all__'


class CourseRetrieveSerializers(ModelSerializer):
    category = CategorySerializers(read_only=True)
    videos = CourseVideoSerializers(source='coursevedio_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


