from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from . import forms, models
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)



@login_required
def add_item(request):
    form = forms.Add_items(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.person = request.user
            form.save()
            return HttpResponseRedirect("/")
        else:
            print('invalid')
    return render(request,'form.html',{'form':form})


@login_required
def list_view(request):
    context = {}
    dataset = models.Shopping_list.objects.all().filter(person=request.user)
    form = forms.DateFilter(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            d = form.cleaned_data['date']
            dataset = models.Shopping_list.objects.all().filter(person=request.user).filter(date=d)

        else:
            print('invalid')
    context = {"dataset":dataset,'form':form}

    return render(request, "index.html", context)


@login_required
def update_view(request, id):

    context = {}
    obj = get_object_or_404(models.Shopping_list, id=id)
    form = forms.Add_items(request.POST or None, instance=obj)
    if (obj.person!=request.user):
        return HttpResponse('You are not authorised')

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    else:
        print('vo')
    context= {"form":form,"obj":obj}
    return render(request, "update_view.html", context)


@login_required
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(models.Shopping_list, id=id)

    if (obj.person!=request.user):
        return HttpResponse('You are not authorised')

    if request.method == "POST":
        # delete object
        obj.delete()

        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)