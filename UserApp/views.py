from django.shortcuts import render, redirect
from UserApp.models import orderDB, SignupDb
from django.contrib import messages


def Home(request):
    return render(request, "Home.html")


def Add_order(request):
    return render(request, "Add_order.html")


def Save_order(request):
    if request.method == "POST":
        name = request.POST.get("name")
        quantiy = request.POST.get("quantity")
        amount = request.POST.get("amount")
        status = request.POST.get("status")
        create = request.POST.get("create")
        update = request.POST.get("update")
        obj = orderDB(Name=name, Quantity=quantiy, Amount=amount, Status=status, CreatedAt=create, UpdatedAt=update)
        obj.save()
        return redirect(Add_order)


def View_orders(request):
    order = orderDB.objects.all()
    return render(request, "View_orders.html", {'order': order})


def Update_order(request, order_id):
    order = orderDB.objects.get(id=order_id)
    return render(request, "Update_order.html", {'order': order})


def Update_orderdetails(request, order_id):
    if request.method == "POST":
        name = request.POST.get("name")
        quantiy = request.POST.get("quantity")
        amount = request.POST.get("amount")
        status = request.POST.get("status")
        create = request.POST.get("create")
        update = request.POST.get("update")
        orderDB.objects.filter(id=order_id).update(Name=name, Quantity=quantiy, Amount=amount, Status=status,
                                                   CreatedAt=create, UpdatedAt=update)
        return redirect(View_orders)


def Delete_order(request, order_id):
    x = orderDB.objects.filter(id=order_id)
    x.delete()
    return redirect(View_orders)


def Sign_in(request):
    return render(request, "Sign_in.html")


def Sign_up(request):
    return render(request, "Sign_up.html")


def Save_signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        pswd = request.POST.get('pass')
        re_pswd = request.POST.get('re_pass')
        obj = SignupDb(Name=name, Email=email, Mobile=mobile, Password=pswd, Repeat_password=re_pswd)
        if SignupDb.objects.filter(Name=name).exists():
            messages.warning(request, "Username already exists")
            return redirect(Sign_in)
        elif SignupDb.objects.filter(Email=email).exists():
            messages.warning(request, "Email already exists")
            return redirect(Sign_in)
        elif SignupDb.objects.filter(Mobile=mobile).exists():
            messages.warning(request, "Mobile Number already exists")
            return redirect(Sign_in)

        obj.save()
        return redirect(Sign_in)


def Signin_check(request):
    if request.method == "POST":
        un = request.POST.get('your_email')
        pswd = request.POST.get('your_pass')
        if SignupDb.objects.filter(Email=un, Password=pswd).exists():
            request.session['Email'] = un
            request.session['Password'] = pswd
            messages.success(request, "Logout Successfully..!")
            return redirect(Home)
        else:
            messages.error(request, "Please try again")
            return redirect(Sign_in)
    else:
        messages.warning(request, "Please try again")
        return redirect(Sign_in)


def Log_out(request):
    del request.session['Email']
    del request.session['Password']
    return redirect(Sign_in)

