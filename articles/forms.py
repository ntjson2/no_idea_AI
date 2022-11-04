from django import forms
from .models import Comment

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

#was forms.ModelForm

class CommentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
       
        self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Comment
        fields = ("comment", "author")

    """ 
    comment = forms.CharField(
        label = "Comment Needed!",
        required = True,
    ) 
    
 """

"""  comment = forms.CharField(
        label = "Comment Needed!",
        required = True,
    ) 
"""

"""      

class ExampleForm(forms.Form):
        prompt = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )

    """