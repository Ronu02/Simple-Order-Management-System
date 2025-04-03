from django.shortcuts import render, redirect
from UserApp.models import orderDB, SignupDb
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


def Dashboard(request):
    order = len(orderDB.objects.all())
    user = len(SignupDb.objects.all())
    time = datetime.datetime.now()
    return render(request, "Dashboard.html", {'order': order, 'user': user, 'time': time})


def View_order(request):
    order = orderDB.objects.all()
    time = datetime.datetime.now()
    return render(request, "View_order.html", {'order': order, 'time': time})


def View_userdetails(request):
    user = SignupDb.objects.all()
    time = datetime.datetime.now()
    return render(request, "View_userdetails.html", {'user': user, 'time': time})


def Admin_login(request):
    return render(request, "Admin_login.html")


def Admin_loginCheck(request):
    if request.method == "POST":
        un = request.POST.get('name')
        pswd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pswd)
            if user is not None:
                login(request, user)
                request.session['username'] = un
                request.session['password'] = pswd
                messages.success(request, "Admin logout successfully")
                return redirect(Dashboard)
            else:
                messages.error(request, "Please try again")
                return redirect(Admin_login)
        else:
            messages.warning(request, "Please try again")
            return redirect(Admin_login)


def Admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Admin_login)

