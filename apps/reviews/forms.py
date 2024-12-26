from django import forms

from apps.reviews.models import Review


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['user']
