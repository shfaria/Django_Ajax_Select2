from django.shortcuts import render
from django.forms import  ModelForm
from django import forms
from .models import Dum, Dim
from django.forms.widgets import SelectMultiple  

class DimForm(forms.Form):
    name = forms.CharField(max_length=50, required=False, widget=forms.Textarea(attrs={'placeholder': 'Bla bla'}))
    dum_choices = [(item.name,item.name) for item in Dum.objects.all()]  
    dum = forms.CharField(max_length=50, required=False, widget=forms.Textarea(attrs={'placeholder': 'Bla bla'}))
    dum = forms.MultipleChoiceField(choices=dum_choices, required=False, widget=forms.SelectMultiple(attrs={'class': 'js-example-basic-multiple'}))


def home(request):
    # dums = Dum.objects.all()
    if request.method == 'POST':
        form = DimForm(request.POST)
        # print(request.POST.getlist('dum'))
        if form.is_valid():
            print("valid")
            dum = form.cleaned_data['dum']
            print(dum)
        else:
            print("not valid")

    else:
        form = DimForm()
    dums = ''
    return render(request, "dummy/home.html", {'form':form, 'dums':dums})