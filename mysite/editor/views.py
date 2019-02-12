from __future__ import print_function
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage
from .forms import ProductForm, UserLoginForm
from .models import Product
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth import authenticate, get_user_model, login, logout
import os
from mysite import settings
lst = []
id_lst = []
# Create your views here.

def editor_view(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    instance = 0
    address = ""
    if form.is_valid():
        img      = Image.open(form.cleaned_data['img'])
        instance = form.save(commit=False)
        instance.save()
        img_format = img.format.lower()
        #instance is Product Type
        try:
            if(type(instance.crop_up)    != type(None) or 
               type(instance.crop_left)  != type(None) or 
               type(instance.crop_low)   != type(None) or 
               type(instance.crop_right) != type(None)):
                tmp = img.crop((instance.crop_up, 
                                instance.crop_left, 
                                instance.crop_low, 
                                instance.crop_right))
                img = tmp
            if(type(instance.resize_x) != type(None) or type(instance.resize_y) != type(None)):
                tmp = img.resize((instance.resize_x,instance.resize_y))
                img = tmp
            if(type(instance.rotate) != type(None)):
                tmp = img.rotate(float(instance.rotate))
                img = tmp
            if(instance.bw == True):
                tmp = img.convert('L')
                img = tmp
            if(instance.share == True):
                name = os.path.join(os.path.dirname(settings.BASE_DIR), "media_cdn")
                name += "/sharedimg%s." % instance.id
                name += img_format
                img.save(name)
                name = "/media/sharedimg%s." % instance.id
                name += img_format
                lst.append(name)
                id_lst.append(instance.id)
        except:
            return HttpResponse("Input is not valid, please return and try again")
        name = os.path.join(os.path.dirname(settings.BASE_DIR), "media_cdn")
        name += "/img%s." % instance.id
        name += img_format
        address = "/media/img%s." %instance.id
        address += img_format 
        img.save(name)
    form = ProductForm()
    context={
        'form':form, 
        'instance':instance,
        'address':address,
    }
    return render(request, "editor_view.html", context)


def shared_page(request):
    lst1 = []
    #lst is all of the sharedimage adreses
    #id_lst is the id of sharedimages
    for i in range(len(lst)):
        tmp = Product.objects.get(id=id_lst[i])
        if(tmp.Admin_share == True):
            lst1.append(lst[i])
    context={
        'lst':lst1
    }
    return render(request, "shared_page.html", context)


def su_shared(request):
    if(request.user.is_authenticated):
        tuples=[]
        for i in range(len(lst)):
            tmp ="http://127.0.0.1:8000/change_sit/%s/" % id_lst[i]
            hlp = Product.objects.get(id=id_lst[i]).Admin_share
            tuples.append((lst[i], tmp, hlp))
        return render(request, 'su_shared.html', {'lst':lst, 'id_lst':id_lst, 'tuples':tuples})
    return HttpResponse("You are not logged in")


def login_view(request):
    if(request.user.is_authenticated):
        return redirect('http://127.0.0.1:8000/su_shared/', {'lst':lst, 'id_lst':id_lst})
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('http://127.0.0.1:8000/su_shared/', {'lst':lst, 'id_lst':id_lst})
    return render(request, 'login_form.html', {"form":form})


def logout_view(request):
    logout(request)
    return redirect("http://127.0.0.1:8000/login")


def change_sit(request, id):
    if(request.user.is_authenticated):
        obj = Product.objects.get(id=id)
        if obj.Admin_share == True:
            obj.Admin_share = False
        else:
            obj.Admin_share = True
        obj.save()
        return redirect("http://127.0.0.1:8000/su_shared/")
    return HttpResponse("You are not logged in")


