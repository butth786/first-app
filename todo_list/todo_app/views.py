from django.shortcuts import render,redirect
from .models import List
from .forms import Listform
from django.contrib import messages
def home(request):
    if request.method == 'POST':
        form = Listform(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,('Item has been added to the List'))
            return render(request,'home.html',{'all_items':all_items})

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('It has been Deleted'))
    return redirect('home')
def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')
def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save
    return redirect('home')