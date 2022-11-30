from django import forms
from .models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Hidden

#was forms.ModelForm

class CommentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.add_input(Hidden("storyLineID", "storyLineID"))

    class Meta:
        model = Comment
        fields = ("comment", "author")
        labels = {"comment": "Storyline",}