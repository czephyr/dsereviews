from django.contrib import admin

from reviews.models import Course, Professor, Review, Teaches


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Teaches)

admin.site.register(Review)
