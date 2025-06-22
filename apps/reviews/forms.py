from django import forms

from apps.reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['user', 'book_id']
        fields = ['content']
        widgets = {
            "content": forms.Textarea(attrs={'class': 'w-full ', 'placeholder': 'Write your review'})
        }
