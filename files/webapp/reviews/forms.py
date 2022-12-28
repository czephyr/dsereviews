from django import forms
from .models import Course, Professor, Review, User
from django_registration.forms import RegistrationForm


class ReviewForm(forms.ModelForm):
    def __init__(self, course, *args, **kwargs):
        super().__init__(*args, **kwargs)
        course = Course.objects.get(id=course.id)
        self.fields["professor"] = forms.ModelChoiceField(
            queryset=course.professor.all()
        )

    lectureStars = forms.IntegerField(
        initial=1, min_value=1, max_value=5, label="Grade the lectures"
    )
    examStars = forms.IntegerField(
        initial=1, min_value=1, max_value=5, label="Grade the exam"
    )
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Review
        fields = ("professor", "text", "lectureStars", "examStars", "emoji")

        widgets = {}


class EmailDomainFilterRegistrationForm(RegistrationForm):
    # List of allowed email domains
    allowed_domain = "studenti.unimi.it"

    def clean_email(self):
        submitted_data = self.cleaned_data["email"]
        domain = submitted_data.split("@")[1]
        if domain != self.allowed_domain:
            raise forms.ValidationError(
                "Only {} emails are allowed.".format(self.allowed_domain)
            )
        if User.objects.filter(email=submitted_data).exists():
            raise forms.ValidationError(
                "This email is already registered."
            )
        return submitted_data
