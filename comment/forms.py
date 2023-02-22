from django import forms
from .models import Comment
from mptt.forms import TreeNodeChoiceField
from captcha.fields import CaptchaField


class NewCommentForm(forms.ModelForm):
    # captcha = CaptchaField()
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["parent"].widget.attrs.update({"class": "d-none"})
        self.fields["parent"].label = ""
        self.fields["parent"].required = False

    class Meta:
        model = Comment
        fields = ("user_name", "parent", "email", "home_page", "text")

        widgets = {
            "user_name": forms.TextInput(attrs={"class": "col-sm-12"}),
            "email": forms.TextInput(attrs={"class": "col-sm-12"}),
            "home_page": forms.TextInput(attrs={"class": "col-sm-12"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
        }

    def save(self, *args, **kwargs):
        Comment.objects.rebuild()
        return super(NewCommentForm, self).save(*args, **kwargs)
