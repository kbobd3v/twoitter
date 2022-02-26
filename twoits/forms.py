from django import forms

from .models import Twoit

MAX_TWOIT_LENGTH = 204

# for this class we're going to use forms from django


class TwoitForm(forms.ModelForm):
    # Model Meta change the behavior of your model fields like changing order options,verbose_name and lot of other options
    class Meta:
        model = Twoit
        # bring content from our Twoit model class
        fields = ['content']

        def clean_content(self):
            # Django forms api have this cleaned_data method to help us pass info in the format we need
            content = self.cleaned_data.get('content')
            if len(content) > MAX_TWOIT_LENGTH:
                forms.ValidationError('This twoit is too long')
            return content
