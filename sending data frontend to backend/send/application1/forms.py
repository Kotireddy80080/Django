from application1.models import student
from django.forms import ModelForm
class student_Forms(ModelForm):
    class Meta:
        model=student
        fields="__all__"
