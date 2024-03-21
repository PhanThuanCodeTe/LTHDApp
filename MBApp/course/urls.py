from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from course import views


r = routers.DefaultRouter()
r.register('categories', views.CategoryViewset, basename='categories')
r.register('courses', views.CourseViewset, basename='course')
r.register('users', views.UserViewset, basename='users')

urlpatterns = [
    path('', include(r.urls)),

]