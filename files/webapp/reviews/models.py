from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg, Count
from django.urls import reverse


class User(AbstractUser):
    bachelor = models.CharField(max_length=70, blank=True)

class Professor(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("reviews:professor_detail", args=[self.slug])

    @property
    def reaction_count(self):
        return (
            self.reviews_professor.values("emoji")
            .annotate(total=Count("emoji"))
            .order_by("total")
            .values("emoji", "total")
        )

    @property
    def lecture_avg(self):
        if self.reviews_professor.aggregate(Avg("lectureStars"))["lectureStars__avg"]:
            return round(
                self.reviews_professor.aggregate(Avg("lectureStars"))[
                    "lectureStars__avg"
                ]
            )
        else:
            return 0

    @property
    def exam_avg(self):
        if self.reviews_professor.aggregate(Avg("examStars"))["examStars__avg"]:
            return round(
                self.reviews_professor.aggregate(Avg("examStars"))["examStars__avg"], 2
            )
        else:
            return 0


class Course(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    field_choices = (
        ("Mathemathics", "Mathemathics"),
        ("Statistics", "Statistics"),
        ("Computer Science", "Computer Science"),
        ("Economics and Finance","Economics and Finance"),
        ("Political Science","Political Science")
    )
    field = models.CharField(max_length=40, choices=field_choices)

    professor = models.ManyToManyField(
        Professor, through="Teaches", related_name="taughtBy"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("reviews:course_detail", args=[self.slug])

    @property
    def reaction_count(self):
        return (
            self.reviews_course.values("emoji")
            .annotate(total=Count("emoji"))
            .order_by("total")
            .values("emoji", "total")
        )

    @property
    def lecture_avg(self):
        if self.reviews_course.aggregate(Avg("lectureStars"))["lectureStars__avg"]:
            return round(
                self.reviews_course.aggregate(Avg("lectureStars"))["lectureStars__avg"],
                2,
            )
        else:
            return 0

    @property
    def exam_avg(self):
        if self.reviews_course.aggregate(Avg("examStars"))["examStars__avg"]:
            return round(
                self.reviews_course.aggregate(Avg("examStars"))["examStars__avg"], 2
            )
        else:
            return 0


class Teaches(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="isTaught"
    )
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, related_name="teaches"
    )


class Review(models.Model):
    emoji_choices = (
        ("😐", "😐"),
        ("😍", "😍"),
        ("🙁", "🙁"),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="is_author")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="reviews_course"
    )
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, related_name="reviews_professor"
    )

    lectureStars = models.PositiveIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    examStars = models.PositiveIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

    emoji = models.CharField(max_length=20, choices=emoji_choices)

    text = models.CharField(max_length=5000)
    created = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created"]

    def __str__(self) -> str:
        return f"By {self.author.id} on {self.course.name}"
