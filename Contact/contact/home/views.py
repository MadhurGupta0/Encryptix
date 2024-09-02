from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render,get_object_or_404,redirect
from . import models
from .form import SignUpForm
from .NewItemForm import NewItemForm,EditItemForm
from django.db.models import Q
from django.contrib import messages


@login_required
def index(request):

    items_exists=models.Item.objects.filter(created_by=request.user).exists()
    if items_exists:
        items=models.Item.objects.filter(created_by=request.user)
        return render(request, 'index.html',{
        'items':items
        })
    else:
        return new(request)
@login_required
def detail(request, pk):
    item = get_object_or_404(models.Item, pk=pk)

    return render(request, 'detail.html', {
        'item': item,
    })
def signup(request):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, (" You Were Signuped"))
            return redirect('login')
        else:
            return render(request,'signup.html',{
                'form': form
            })
    form=SignUpForm()
    return render(request, 'signup.html',{
        'form': form
    })
@login_required
def new(request):
    if request.method=="POST":
        if request.FILES:
         form=NewItemForm(request.POST,request.FILES)
        else:
            form=NewItemForm(request.POST)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            messages.success(request, ("new item created"))
            return redirect("detail",pk=item.id)
        form.save()
        return render(request, 'form.html',{
        'form': form,
        'title': 'New Item',
    })
    form=NewItemForm()
    return render(request, 'form.html',{
        'form': form,
        'title': 'New Item',
    })

@login_required
def delete(request ,pk):

    itm=get_object_or_404(models.Item,pk=pk, created_by= request.user)
    itm.delete()
    messages.success(request, (" Item was Deleted"))
    return redirect("index")

@login_required
def edit(request,pk):
    itm = get_object_or_404(models.Item, pk=pk, created_by=request.user)
    if request.method=="POST":
        if request.FILES:
         form=EditItemForm(request.POST,request.FILES,instance=itm)
        else:
            form=EditItemForm(request.POST,instance=itm)
        if form.is_valid():
            form.save()
            messages.success(request, ("Edit were done"))
            return redirect("detail",pk=itm.id)
    else:
     form=EditItemForm(instance= itm)
    return render(request, 'form.html',{
        'form': form,
        'title': 'Edit Item',
    })


@login_required
def item(request):
    query= request.GET.get('query','')


    if query:
         items =models.Item.objects.filter(created_by=request.user)
         items=items.filter(Q(name__icontains=query))
    else:
     items=models.Item.objects.filter(created_by=request.user)

    return render(request,"items.html",{
        'items': items,
        'query': query,
    })

@login_required
def lout(request):
    logout(request)
    messages.success(request," You were loged Out")
    return redirect('login')


