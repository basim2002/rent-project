from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from basim.forms import Districtform, Areaform, Bookform, Customer_form, Dealer_form, Book_category_form, Feedback_form, \
    Replay_form
from basim.models import District, Book, Area, Login, Book_Category, Feedback


# Create your views here.
def index1(request):
    return render(request,'index1.html')

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        print(username)
        password=request.POST.get('pass')
        print(password)
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            if user.is_user:
                return redirect('dashboad')
            elif user.is_customer:
                return redirect('customer_home')

            elif user.is_dealer:
                return redirect('dealer_home')

            else:
                messages.info(request, 'invalid credentials')

    return render(request, 'login.html')

def add_customer(request):
    form=Customer_form()
    if request.method=='POST':
        form=Customer_form(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_customer=True
            user.save()
            return redirect('login')
    return render(request,'customer/cust_register.html',{'form':form})

def add_dealer(request):
    form=Dealer_form()
    if request.method=='POST':
        form=Dealer_form(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_dealer=True
            form.save()
            return redirect('login')

    return render(request,'admin/add_dealer.html',{'form':form})


def dashboad(request):
    return render(request,'admin/dashboad.html')

def customer_home(request):
    return render(request,'customer/customer_home.html')

def dealer_home(request):
    return render(request,'dealer/dealer_home.html')

def adddistrict(request):
    form=Districtform()
    if request.method=='POST':
        form=Districtform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('districtview')
    return render(request,'admin/adddis.html',{'form':form})

def addarea(request):
    form=Areaform()
    if request.method=='POST':
        form=Areaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewarea')
    return render(request,'admin/addarea.html',{'form':form})

def addbook(request):
    form=Bookform()
    if request.method=='POST':
        form=Bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dealer_book_view')
    return render(request,'dealer/addbook.html',{'form':form})

def add_book_category(request):
    form=Book_category_form()
    if request.method=='POST':
        form=Book_category_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_book_category')
    return render(request,'admin/add_book_category.html',{'form':form})

def view_book_category(request):
    data=Book_Category.objects.all()
    return render(request,'admin/view_book_category.html',{'data':data})

def view_cust_bookcategory(request):
    data=Book_Category.objects.all()
    return render(request,'customer/view_cust_bookcategory.html',{'data':data})

def delete_book_category(request,id):
    data=Book_Category.objects.get(id=id)
    data.delete()
    return redirect('view_book_category')

def view_customer(request):
    data=Login.objects.filter(username=request.user)
    return render(request,'customer/view_customer.html',{'data':data})

def view_customer_admin(request):
    data=Login.objects.filter(is_customer=True)
    return render(request,'admin/view_customer_admin.html',{'data':data})


def admin_view_dealer(request):
    data=Login.objects.all()
    return render(request,'admin_view_dealer.html',{'data':data})


def view_dealer(request):
    data=Login.objects.filter(username=request.user)
    return render(request,'dealer/view_dealer.html',{'data':data})




def districtview(request):
    data=District.objects.all()
    return render(request,'admin/districtview.html',{'data':data})

def viewarea(request):
    data=Area.objects.all()
    return render(request,'admin/viewarea.html',{'data':data})

def viewbook(request):
    data=Book.objects.all()
    return render(request,'admin/viewbook.html',{'data':data})

def districtdelete(request,id):
    data=District.objects.get(id=id)
    data.delete()
    return redirect('districtview')

def deletearea(request,id):
    data=Area.objects.get(id=id)
    data.delete()
    return redirect('viewarea')

def deletebook(request,id):
    data=Book.objects.get(id=id)
    data.delete()
    return redirect('viewbook')

def delete_customer(request,id):
    data=Login.objects.get(id=id)
    data.delete()
    return redirect('view_customer')

def editbook(request,id):
    data=Book.objects.get(id=id)
    form=Bookform(instance=data)
    if request.method=='POST':
        form=Bookform(request.POST or None,instance=data)
        if form.is_valid():
            form.save()
            return redirect('dealer_book_view')
    return render(request,'dealer/editbook.html',{'form':form})

def cust_book_view(request):
    data=Book.objects.all()
    return render(request,'customer/cust_book_view.html',{'data':data})

def dealer_book_view(request):
    data=Book.objects.all()
    return render(request,'dealer/dealer_book_view.html',{'data':data})


def add_feedback(request):
    form=Feedback_form()
    if request.method=='POST':
        form=Feedback_form(request.POST)
        if form.is_valid():

            form.save()
            return redirect('cust_view_feedback')
    return render(request,'customer/add_feedback.html',{'form':form})

def admin_view_feedback(request):
    data=Feedback.objects.all()
    return render(request,'admin/admin_view_feedback.html',{'data':data})

def cust_view_feedback(request):
    data=Feedback.objects.filter(username=request.user)
    return render(request,'customer/cust_view_feedback.html',{'data':data})

def dealer_view_feedback(request):
    data=Feedback.objects.all()
    return render(request,'dealer/dealer_view_feedback.html',{'data':data})

def dealer_view_cust(request):
    data=Login.objects.filter(is_customer=True)
    return render(request,'dealer/dealer_view_cust.html',{'data':data})

def dealer_view_category(request):
    data=Book_Category.objects.all()
    return render(request,'dealer/dealer_view_category.html',{'data':data})



def view_replay(request):
    data=Feedback.objects.all()
    return render(request,'customer/view_replay.html',{'data':data})



def replay_feedback(request):
    form=Replay_form()
    if request.method=='POST':
        form=Replay_form(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'admin/replay_feedback.html',{'form':form})



def profile(request):
    data=Login.objects.filter(username=request.user)
    print(data)
    return render(request,'customer/view_profile.html',{'data':data})

def logout_view(request):
    logout(request)
    return redirect('login')
