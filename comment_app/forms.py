from django import forms
from comment_app.models import Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]
        widgetd = {
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }



