from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Expense
from .forms import ExpenseForm

def register_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        confirm=request.POST['confirm']

        if password != confirm:
            return HttpResponse("Miss match password,TRY AGAIN")
        else:
            user=User.objects.create_user(username=username,password=password)
            return redirect('login')    
    else:
        return render(request,'register.html')    

def login_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("login failed")    
    else:
        return render(request,'login.html')
   
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def expense_chart(request):
    if request.method == 'POST':
        form=ExpenseForm(request.POST)
        if form.is_valid():
            expense=form.save(commit=False)
            expense.user=request.user
            expense.save()
            return redirect('sheet')
    else:
        form=ExpenseForm()
    return render(request,'chart3.html',{'form':form})

def home(request):
    return render(request,'home.html')

@login_required
def sheet_view(request):
    query=request.GET.get('q')
    expenses=Expense.objects.filter(user=request.user)
    if query:
        expenses=expenses.filter(
        Q(title__icontains=query)|
        Q(category__icontains=query)|
        Q(amount__icontains=query)
    )
    return render(request,"sheet.html",{'expenses':expenses,'query':query})

def delete(request,expense_id):
    expense=get_object_or_404(Expense,id=expense_id)
    expense.delete()
    return redirect('sheet')
