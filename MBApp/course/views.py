from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from course.models import Course, Category, Lesson, User
from course import serializers, paginators


class CategoryViewset(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CourseViewset(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = serializers.CourseSerializer
    pagination_class = paginators.CourseSetPagination

    def get_queryset(self):
        queryset = self.queryset

        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)

        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            queryset = queryset.filter(category_id=cate_id)

        return queryset


@action(methods=['get'], url_path='lessons', detail=True)
def get_lessons(self, request, pk):
    lessons = self.get_object().lesson_set.filter(active=True)

    return Response(serializers.LessonSerializer(lessons, many=True).data, status=status.HTTP_200_OK)


# class LessonViewset(viewsets.ViewSet, generics.RetrieveAPIView):
#     queryset = Lesson.objects.prefetch_related('tags').filter(acitve=True)
#     serializer_class = serializers.LessonDetailsSerializer
class UserViewset(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer
