from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Data, Land, Blog, Request, Served_Request, Crop, Message
# from django.core.mail import send_mail

loggedin_farmer = {}


def index(request):
#     send_mail(
#     'Subject here',
#     'Here is the message.',
#     'from@example.com',
#     ['dibyojyoti21century@gmail.com'],
#     fail_silently=False,
# )
    return render(request, 'dbms/index.html', {'blogs': Blog.objects.all()})

def farmerSearch(request):
    return render(request, 'dbms/searchFarmer.html', {'lands': Land.objects.all()})

def signup(request):
    return render(request, 'dbms/signup.html')


def login(request):
    if request.method == 'POST':
        data = request.POST.dict()
        user_name = data.get("user_name")
        password = data.get("password")
        try:
            farmer = Data.objects.get(pk=user_name)
        except Data.DoesNotExist:
            return render(request, 'dbms/index.html', {'username_status': 'Username DOES NOT EXIST!', 'username': user_name})
            #raise Http404("Incorrect  User Name")
        if(farmer.password == password):
            global loggedin_farmer
            loggedin_farmer = farmer
            return HttpResponseRedirect('/dbms/dashboard/')
            # return dashboard(request, farmer)
            # return render(request, 'dbms/dashboard.html', {'farmer': farmer})
        else:
            return render(request, 'dbms/index.html', {'pwd_status': 'INCORRECT PASSWORD!', 'username': user_name})
    else:
        return render(request, 'dbms/index.html')

def logout(request):
    if request.method == 'POST':
        global loggedin_farmer
        loggedin_farmer = {}
        return HttpResponseRedirect('/dbms/')

def message(request):
    if request.method == 'POST':
        data = request.POST.dict()
        message = Message(
            name = data.get('Name'),
            mobile_number = data.get('Mobile'),
            subject = data.get('Subject'),
            message = data.get('Message'),
        )
        message.save()
        return HttpResponseRedirect('/dbms/')

def submit(request):
    if request.method == 'POST':
        data = request.POST.dict()
        username = data.get("user_name")
        try:
            farmer = Data.objects.get(pk = username)
        except Data.DoesNotExist:
            if(data.get('password') != data.get('confirm_password')):
                return render(request, 'dbms/index.html',{'pwd_status': 'PASSWORDS DO NOT MATCH', 'data': data,'blogs': Blog.objects.all() })
            
            farmer = Data(
            name=data.get('name'),
            mobile_number=data.get('mobile_number'),
            residence=data.get('residence'),
            aadhar=data.get('aadhar'),
            user_name=data.get('user_name'),
            password=data.get('password'),
            )
            farmer.save()
            # return HttpResponse("%s Thanks for Registering with us !" % Name)
            return render(request, 'dbms/index.html', {'success': data, 'signup_status': 'Successfull', 'message' : 'Thanks for registering with us !!!','blogs': Blog.objects.all()})

        else:
            return render(request, 'dbms/index.html',{'username_status': 'USERNAME ALREADY EXISTS ! TRY SOMETHING ELSE...', 'data': data, 'blogs': Blog.objects.all()})



def dashboard(request):
    global loggedin_farmer
    username = loggedin_farmer.user_name
    return render(request, 'dbms/dashboard.html', {'farmer': loggedin_farmer, 'lands': Land.objects.filter(user_name=username), 'crops': Crop.objects.all()})


def add_land(request):
    if request.method == 'POST':
        data = request.POST.dict()
        global loggedin_farmer
        user_name = loggedin_farmer.user_name
        for land in Land.objects.filter(user_name=user_name):
            if land.land_address.lower() == data.get('land_address').lower():
                if land.land_name.lower() == data.get('land_name').lower():
                    return HttpResponseRedirect('/dbms/dashboard/')
        land_data = Land(
            user_name=loggedin_farmer,
            land_name=data.get('land_name'),
            land_address=data.get('land_address'),
            district = data.get('district'),
            soil_type=data.get('soil_type'),
            crop_grown=data.get('crop_grown'),
            moisture_requirement = data.get('moisture_requirement'),
            threshold_moisture = data.get('threshold_moisture'),
            expected_yield = data.get('expected_yield'),
            expected_price = data.get('expected_price'),
        )
        land_data.save()
        return HttpResponseRedirect('/dbms/dashboard/')

def request_irrigation(request):
    if request.method == 'POST':
        data = request.POST.dict()
        global loggedin_farmer
        req_data = Request(
            user_name = loggedin_farmer,
            land_name = data.get('land_name'),
            land_address = data.get('land_address'),
            district = data.get('district')
        )
        req_data.save()
        return HttpResponseRedirect('/dbms/dashboard/')

def cancel_request(request):
    if request.method == 'POST':
        data = request.POST.dict()
        global loggedin_farmer
        req_data = Request.objects.get(user_name = loggedin_farmer,land_name = data.get('land_name'),land_address = data.get('land_address'),district = data.get('district'))
        land = Land.objects.get(user_name = loggedin_farmer,land_name = data.get('land_name'),land_address = data.get('land_address'),district = data.get('district'))
        req_data.delete()
        land.request_status = 'False'
        land.save()
        return HttpResponseRedirect('/dbms/dashboard/')

def deactivate_request(request):
    if request.method == 'POST':
        data = request.POST.dict()
        global loggedin_farmer
        req_data = Served_Request.objects.get(user_name = loggedin_farmer,land_name = data.get('land_name'),land_address = data.get('land_address'),district = data.get('district'))
        land = Land.objects.get(user_name = loggedin_farmer,land_name = data.get('land_name'),land_address = data.get('land_address'),district = data.get('district'))
        req_data.delete()
        land.request_status = 'False'
        land.system_id = 'None'
        land.save()
        return HttpResponseRedirect('/dbms/dashboard/')

def delete_land(request):
    if request.method == 'POST':
        data = request.POST.dict()
        global loggedin_farmer
        try:
            req_data = Served_Request.objects.get(user_name = loggedin_farmer,land_name = data.get('land_name'),land_address = data.get('land_address'),district = data.get('district'))
            req_data.delete()
        except Served_Request.DoesNotExist:
            pass
        try:
            req = Request.objects.get(user_name = loggedin_farmer,land_name = data.get('land_name'),land_address = data.get('land_address'),district = data.get('district'))
            req.delete()
        except Request.DoesNotExist:
            pass
        land = Land.objects.get(user_name = loggedin_farmer,land_name = data.get('land_name'),land_address = data.get('land_address'),district = data.get('district'))
        land.delete()
        return HttpResponseRedirect('/dbms/dashboard/')

