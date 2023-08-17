from django.shortcuts import render
from django.forms import  ModelForm
from django import forms
from .models import Dum, Dim
from django.forms.widgets import SelectMultiple  
import json
from django.http import JsonResponse

class DimForm(forms.Form):
    name = forms.CharField(max_length=50, required=False, widget=forms.Textarea(attrs={'placeholder': 'Bla bla'}))
    dum_choices = [(item.name,item.name) for item in Dum.objects.all()]  
    dum = forms.CharField(max_length=50, required=False, widget=forms.Textarea(attrs={'placeholder': 'Bla bla'}))
    dum = forms.MultipleChoiceField(choices=dum_choices, required=False, widget=forms.SelectMultiple(attrs={'class': 'js-example-basic-multiple'}))

class CreationForm(ModelForm):
    class Meta:
        model = Dim
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dum'].queryset = Dum.objects.none()

        if 'name' in self.data:
            self.fields['dum'].queryset = Dum.objects.all()
        elif self.instance.pk :
            self.fields['dum'].queryset = Dum.objects.all().filter(pk=self.instance.dum.pk)

            

def home0(request):
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

def dumView(request):
    return render(request, "dummy/dum.html")


def home(request):
    form = CreationForm()
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("form valid and saved")
        else:
            print("not valid")

    else:
        form = DimForm()

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        term = request.GET.get('term')
        dums = Dum.objects.all().filter(name__icontains=term)
        return JsonResponse(list(dums.values()), safe=False)
    dums = ''
    return render(request, "dummy/home.html", {'form':form, 'dums':dums})