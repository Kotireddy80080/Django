from application1.models import employees
from django.forms import ModelForm 
class employees_Forms(ModelForm):
    class Meta:
        model=employees 
        fields="__all__"