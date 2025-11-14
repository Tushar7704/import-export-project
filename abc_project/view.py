from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from django.contrib import messages

from srvc.models import *
from export_dyp.models import *
from delivery_team.models import *
from import_dyp.models import *
from track.models import *

def singin(request):
    if request.method == "POST":
        username = request.POST.get("lusername")
        password = request.POST.get("lpassword")

        try:
            user = register.objects.get(runame=username, rconpass=password)
            if user.rconpass == password:
                messages.success(request, f"Welcome {user.runame}")
                return redirect('/')
            else:
                messages.error(request, 'Invalid Username or Password!')
                return render(request, 'login.html')

        except register.DoesNotExist:
            messages.error(request, 'Invalid Username or Password!')
            return render(request, 'login.html')
    return render(request, 'login.html')

def singout(request):
    logout(request)
    return redirect("/") 

def rgst(request):
    if request.method=="POST":
        rn=request.POST.get('rgname')
        run=request.POST.get('rgusername')
        remail=request.POST.get('rgemail')
        rnum=request.POST.get('rgnumber')
        rcpass=request.POST.get('rgcpass')
        rcnpass=request.POST.get('rgconpass')
        if rcpass == rcnpass:
            sv=register(rname=rn,
                        runame=run,
                        remail=remail,
                        rmobile=rnum,
                        rcrtpass=rcpass,
                        rconpass=rcnpass)
            sv.save()
            messages.info(request, 'Your Registration successfully!')
            return redirect("login")
        else:
            messages.error(request, "Your password is not same!")
            return render(request, 'register.html')
    return render(request,"register.html")

def Home(request):
    teamdata=team.objects.all()
    servicedata=service.objects.all()
    clientdata=client.objects.all()
    data={
        'teamdata':teamdata,
        'servicedata':servicedata,
        'clientdata':clientdata,
    }
    return render(request,"index.html",data)

def AboutUs(request):
    return render(request,"about.html")

def Service(request):
    servicedata=service.objects.all()
    AirFreightdata=AirFreight.objects.all()
    OceanFreightdata=OceanFreight.objects.all()
    LandTransportdata=LandTransport.objects.all()
    CargoStoragedata=CargoStorage.objects.all()
    data={
        'servicedata':servicedata,
        'AirFreightdata':AirFreightdata,
        'OceanFreightdata':OceanFreightdata,
        'LandTransportdata':LandTransportdata,
        'CargoStoragedata':CargoStoragedata,
    }
    return render(request,"service.html",data)

def Price(request):
    return render(request,"price.html")

def Import(request):
    return render(request,"import.html")

def Hardware(request):
    hardwaredta=hardware.objects.all()
    data={
        'hardwaredta':hardwaredta,
    }
    return render(request,"hardware.html",data)

def Software(request):
    return render(request,"software.html")

def Crude(request):
    crudData=crudoil.objects.all()
    data={
        'crudData':crudData,
    }
    return render(request,"crude.html",data)

def Motor(request):
    motordata=motor.objects.all()
    motordata3=motorspl.objects.all()
    data={
        'motordata':motordata,
        'motordata3':motordata3,
    }
    return render(request,"motor-vehicle.html",data)

def Mechanical(request):
    mechanicaldata=mechanical.objects.all()
    data={
        'mechanicaldata':mechanicaldata,
    }
    return render(request,"mechanical.html",data)

def Export(request):
    productsdata=ExportProduct.objects.all()
    # for a in productsdata:
    #     print(a.eximg)
    # print(productsdata)
    data={
        'productsdata':productsdata,
    }
    return render(request,"export.html",data)

def Exform(request):
    if request.method=="POST":
        ecn=request.POST.get('customerName')
        ee=request.POST.get('email')
        en=request.POST.get('number')
        ep=request.POST.get('product')
        eq=request.POST.get('quantity')
        ec=request.POST.get('country')
        esa=request.POST.get('address-20')
        epym=request.POST.get('payment')
        sv=ExportForm(CustomerName=ecn,
                      Email=ee,
                      contact=en,
                      Product=ep,
                      Quantity=eq,
                      Country=ec,
                      Shipping=esa,
                      Payment=epym)
        sv.save()
        return redirect("exorder")
    else:
        return render(request, "ex-form.html")

def Contact(request):
    if request.method=="POST":
        cn=request.POST.get('cname')
        ce=request.POST.get('cemail')
        cs=request.POST.get('csubject')
        cm=request.POST.get('cmessage')
        sv=contact(cname=cn,
                   cemail=ce,
                   csub=cs,
                   cmsg=cm)
        sv.save()
    return render(request,"contact.html")

def Feedback(request):
    if request.method=="POST":
        fbn=request.POST.get('fbname')
        fbe=request.POST.get('fbemail')
        fbno=request.POST.get('fbnumber')
        fbs=request.POST.get('fbservice')
        fbm=request.POST.get('fbmessage')
        sv=FeedBack(fbname=fbn,
                    fbemail=fbe,
                    fbnum=fbno,
                    fbsrv=fbs,
                    fbmsg=fbm)
        sv.save()
    return render(request,"feedback.html")

def Register(request):
    return render(request,"register.html")

def Login(request):
    return render(request,"login.html")

def Forget(request):
    return render(request,"forget.html")

def Learn(request):
    return render(request,"learn-m.html")


def impform(request):
    if request.method=="POST":
        icn=request.POST.get('customerName')
        ie=request.POST.get('email')
        ic=request.POST.get('number')
        ip=request.POST.get('product')
        iq=request.POST.get('quantity')
        ist=request.POST.get('state')
        isa=request.POST.get('address-20')
        ipym=request.POST.get('payment')
        sv=ImportForm(CustomerName=icn,
                      Email=ie,
                      contact=ic,
                      Product=ip,
                      Quantity=iq,
                      St=ist,
                      Shipping=isa,
                      Payment=ipym)
        sv.save()
        return redirect("importform")
    else:
        return render(request, "import_form.html")

def track(request):
    if request.method == "POST":
        pid = request.POST.get("txttrackid")

        product = ProductDetail.objects.filter(id=pid)
        if product.exists():
            return render(request, "track.html", {
                'product':product,
                'pid':pid,
            })
        else:
            return render(request, "track.html", {
                'product':product,
                'pid':pid,
                'messages':'No product found!'
            })
    else:
        return render(request, "index.html")