from django.shortcuts import redirect, render
from item.models import Category, Item
from django.contrib.auth import logout as lg

from .forms import SignUpForm

def logout(request):
    lg(request)
    return render(request, 'core/logout.html')

def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {
        "form": form,
    })