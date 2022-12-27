from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from reviews.forms import ReviewForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from reviews.models import Course, Professor, User


class HomeView(View):
    def get(self, request):
        courses = Course.objects.all()
        professors = Professor.objects.all()
        context = {"courses_all": courses, "professors_all": professors}
        return render(request, "home.html", context)


class CourseDetail(View):
    def get(self, request, slug):
        course = get_object_or_404(Course, slug=slug)
        reviews = course.reviews_course.filter(active=True).order_by("-id")
        paginator = Paginator(reviews, 5)
        page = request.GET.get("page")
        try:
            reviews_in_page = paginator.page(page)
        except PageNotAnInteger:
            reviews_in_page = paginator.page(1)
        except EmptyPage:
            reviews_in_page = paginator.page(paginator.num_pages)

        if request.user.is_authenticated:
            review_form = ReviewForm(course)

            context = {
                "course": course,
                "page": page,
                "reviews": reviews_in_page,
                "review_form": review_form,
            }
        else:
            context = {"course": course, "page": page, "reviews": reviews_in_page}

        return render(request, "course_detail.html", context)

    def post(self, request, slug):
        course = get_object_or_404(Course, slug=slug)
        review_form = ReviewForm(course, request.POST)

        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.author = request.user
            new_review.course = course
            new_review.save()
        return HttpResponseRedirect(self.request.path_info)


class ProfessorDetail(View):
    def get(self, request, slug):
        professor = get_object_or_404(Professor, slug=slug)
        reviews = professor.reviews_professor.filter(active=True).order_by("-id")
        paginator = Paginator(reviews, 5)
        page = request.GET.get("page")
        try:
            reviews_in_page = paginator.page(page)
        except PageNotAnInteger:
            reviews_in_page = paginator.page(1)
        except EmptyPage:
            reviews_in_page = paginator.page(paginator.num_pages)

        context = {"professor": professor, "page": page, "reviews": reviews_in_page}

        return render(request, "professor_detail.html", context)


def shihab(request):
    return HttpResponse("Inspired by SHB")
