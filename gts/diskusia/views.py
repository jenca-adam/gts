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
      
    paginator=Paginator(Prispevok.objects.all().order_by('-vznikol'),10)
    pageint=int(page)
    pagenormalized=min(max(pageint,1),paginator.num_pages)
    template=loader.get_template('diskusia/prispevky.html')
    if pageint != pagenormalized:
        return HttpResponseRedirect('/diskusia/{}'.format(pagenormalized))
    context={
        'prispevky':paginator.page(pageint).object_list,

        'form':form,
        'nextpage':pageint+1,
        'prevpage':pageint-1,
        'firstpage':1,
        'lastpage':paginator.num_pages,
        'curpage':page
    }
    return HttpResponse(template.render(context,request))
