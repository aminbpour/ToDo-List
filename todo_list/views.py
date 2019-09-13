from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ListForm
from .models import List
# Create your views here.


def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST)

        if form.is_valid():
            form.save()
            all_items = List.objects.all

            messages.success(request, 'Item Has Been Added To List')

            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def delete(request, item_id):
    item = List.objects.get(pk=item_id)
    item.delete()
    messages.success(request, 'Item Has Been Deleted')
    return redirect('home')


def cross_off(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = False
    item.save()
    return redirect('home')


def edit(request, item_id):
    item = List.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Item Edited')
            return redirect('home')

    else:
        item = List.objects.get(pk=item_id)
        return render(request, 'edit.html', {'item': item})
