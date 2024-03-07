from django.contrib import admin
from course.models import Category, Course
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from cloudinary.models import CloudinaryField


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'updated_date', 'active']
    search_fields = ['name', 'description']
    readonly_fields = ['my_images']
    form = CourseForm

    class Media:
        css = {'all': ['/static/css/style.css'], }
        js = ('/static/js/script.js', )

    def my_images(self, course):
        if course.image:
            return mark_safe(f"<img width='400' src='{course.image.url}' />")


admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
