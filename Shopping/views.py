from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import forms, models
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)



@login_required
def add_item(request):
    form = forms.Add_items_form(request.POST)
    model = models.Shopping_list
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            status = form.cleaned_data['status']
            date_f = form.cleaned_data['date']
            p = model(item_name=name,item_quantity=quantity,item_status=status,date=date_f,person=request.user)
            p.save()
            return HttpResponseRedirect("/")
        else:
            print('invalid')
    return render(request, 'add_item.html', {'form':form})


@login_required
def list_view(request):
    dataset = models.Shopping_list.objects.all().filter(person=request.user).order_by('date')
    dataset = dataset.reverse()

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
def update_view(request,person,item_name,id):

    context = {}
    obj = get_object_or_404(models.Shopping_list, id=id)
    print(type(obj))
    form = forms.Update_items(request.POST or None, instance=obj)
    if (obj.person!=request.user):
        return HttpResponse('You are not authorised')

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context= {"form":form,"obj":obj}
    return render(request, "update_item.html", context)


@login_required
def delete_view(request,person,item_name,id):
    context = {}
    obj = get_object_or_404(models.Shopping_list, id=id)

    if (obj.person!=request.user):
        return HttpResponse('You are not authorised')

    if request.method == "POST":
        # delete object
        obj.delete()

        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)