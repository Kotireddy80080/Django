from django import forms
class employee_Regestration(forms.Form):
    eid=forms.IntegerField(label="eid")
    ename=forms.CharField(label="ename",max_length=21)
    esal=forms.FloatField(label="esal")
    company=forms.CharField(label="company",max_length=21)
    email=forms.EmailField(label="email")
    j_date=forms.DateField(label="j_date")