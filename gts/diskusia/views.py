from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User,Prispevok
from django.template import loader
from django import forms

class PrispevokForm(forms.Form):

    obsah = forms.CharField(label="Príspevok",max_length=500,widget=forms.Textarea)

def index(request):

    if request.method=='POST':
        form=PrispevokForm(request.POST)
        if form.is_valid():
            adam=User.objects.get(username='adam')
            prispevok=Prispevok(obsah=form.cleaned_data['obsah'],uzivatel=adam)
            prispevok.save()
            return HttpResponseRedirect('/')
    else:
        form=PrispevokForm()
    template=loader.get_template('diskusia/prispevky.html')
    context={
        'prispevky':Prispevok.objects.all().order_by('-vznikol'),
        'form':form,
    }
    return HttpResponse(template.render(context,request))
