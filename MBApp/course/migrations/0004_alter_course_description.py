# Generated by Django 5.0.3 on 2024-03-07 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0003_alter_course_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="description",
            field=models.TextField(default=" ", null=True),
        ),
    ]