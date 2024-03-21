from course.models import Category, Course, Lesson, User
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ItemsSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = instance.image.url

        return rep


class CourseSerializer(ItemsSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'image', 'created_date']


class LessonSerializer(ItemsSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'created_date']


class LessonDetailsSerializer(LessonSerializer):
    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['tags', 'content']


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'avatar']
        extra_kwargs = {
            'password':{
                'write_only': 'true'
            }
        }