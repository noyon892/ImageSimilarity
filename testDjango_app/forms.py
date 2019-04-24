from difflib import SequenceMatcher

from PIL import Image
from django.forms import ModelForm
from django import forms
from pytesseract import pytesseract

from testDjango_app.models import Person


class PostForm(ModelForm):
    class Meta:
        model = Person
        fields = ["name", "department", "image", "image2"]

    def clean(self):
        super(PostForm, self).clean()
        name = self.cleaned_data.get('name')
        image = self.cleaned_data.get('image')
        image2 = self.cleaned_data.get('image2')

        text = pytesseract.image_to_string(Image.open(image)).lower()
        text2 = pytesseract.image_to_string(Image.open(image2)).lower()
        ratio = SequenceMatcher(a=text, b=text2).ratio() * 100

        if len(name) < 5:
            self._errors['name'] = self.error_class(['Minimum 5 characters required'])
        if ratio == 100:
            self._errors['image'] = self.error_class(['First Image can\'t be Same as 2nd image'])
            self._errors['image2'] = self.error_class(['Second Image can\'t be Same as 1st image'])

        return self.cleaned_data
