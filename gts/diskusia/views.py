from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User,Prispevok
from django.template import loader
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

class PrispevokForm(forms.Form):

    obsah = forms.CharField(label="Príspevok",max_length=500,widget=forms.Textarea)

@login_required
def index(request,page='1'):
    
    if request.method=='POST':
        form=PrispevokForm(request.POST)
        if form.is_valid():
            prispevok=Prispevok(obsah=form.cleaned_data['obsah'],uzivatel=request.user)
            prispevok.save()
            return HttpResponseRedirect('/diskusia')
    else:
        form=PrispevokForm()
    paginator=Paginator(10,Prispevok.objects.all())
    template=loader.get_template('diskusia/prispevky.html')
    context={
        'prispevky':paginator,
        'form':form,
    }
    return HttpResponse(template.render(context,request))
