# Generated by Django 4.1.9 on 2023-06-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("university_app", "0010_remove_course_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="slug",
            field=models.SlugField(default="<django.db.models.fields.CharField>", unique=True),
        ),
    ]