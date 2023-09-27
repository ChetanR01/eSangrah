from django.shortcuts import render, redirect
from .models import Product, Contact, Offer, Fruit, Electronic, Xerox, DryFruit, Vegetable, DailyNeed, Stationary
from datetime import datetime
from django.contrib.auth.models import User, auth 

# Create your views here.

def index(request):
    products = Product.objects.all().order_by("-id")
    offers = Offer.objects.all().order_by("-id")
    return render(request, 'index.html' ,{"products":products, "offers":offers})

def fruits(request):
    fruits = Fruit.objects.all().order_by("-id")
    return render(request, 'fruits.html', {"fruits":fruits})

def dryfruit(request):
    dryfruits = DryFruit.objects.all().order_by("-id")
    return render(request, 'dryfruit.html', {"dryfruits":dryfruits})

def vegetable(request):
    vegetables = Vegetable.objects.all().order_by("-id")
    return render(request, 'vegetable.html', {"vegetables":vegetables})

def dailyneed(request):
    dailyneeds = DailyNeed.objects.all().order_by("-id")
    return render(request, 'dailyneed.html', {"dailyneeds":dailyneeds})

def electronics(request):
    electronics = Electronic.objects.all().order_by("-id")
    return render(request, 'electronics.html', {"electronics":electronics})

def stationary(request):
    stationarys = Stationary.objects.all().order_by("-id")
    return render(request, 'stationary.html', {"stationarys":stationarys})

def xerox(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        desc=request.POST.get('desc')
        file=request.POST['file']

        xeroxs = Xerox.objects.create(name=name, phone=phone, desc=desc, file=file, date=datetime.now())
        xeroxs.save()
        return redirect("/")
    return render(request, 'xerox.html')    

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST.get('desc')

        contacts = Contact.objects.create(name=name, email=email, phone=phone, desc=desc, date=datetime.now())
        contacts.save()
        return redirect("/")
    return render(request, 'contact.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":
            name=request.POST["name"]
            email=request.POST["email"]
            password=request.POST["password"]
            confirm_pass=request.POST["confirm_pass"]
            if password==confirm_pass:
                User.objects.create_user(first_name=name,email=email,username=email,password=password)
                print("User Created")
                return redirect("/login")
            else:
                print("Password does not match")
                return redirect("/signup")
        else:
            return render(request,"signup.html")

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user= auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            print("Invalid Password")
            return redirect("/login")

    return render(request, 'login.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("/")