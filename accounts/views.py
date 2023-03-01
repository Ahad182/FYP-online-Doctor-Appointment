from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import logout

from accounts.models import BloodModel, GenderModel, User

# Create your views here.


def loginuser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username , password=password)
        
        if user is not None:

            auth.login(request,user)
            messages.success(request, "login successfully")
            return redirect('home')
        else:
            messages.error(request, "plez enter correct information")
            return redirect('login')
   
        
    return render(request, 'accounts/login.html')




def register(request):
    blood_group = BloodModel.objects.all()
    gender_group = GenderModel.objects.all()
    if request.method == 'POST':
        username= request.POST.get('username')
        fname= request.POST.get('first_name')
        middle_name= request.POST.get('middle_name')
        last_name= request.POST.get('last_name')
        father_name= request.POST.get('father_name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        blood= request.POST.get('blood')
        gender= request.POST.get('gender')
        address= request.POST.get('address')
        password= request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')
        if password == confirm_password :
           
            if User.objects.filter(username=username).exists():

                messages.error(request,"username Allready exist")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"email Allready exist")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password,first_name=fname,m_name=middle_name,last_name=last_name,phone=phone,address=address, father_name=father_name,gender=gender,blood=blood )
                    # auth.login(request,user)
                    user.save()
                    messages.success(request,"Register successfully")
                    return redirect('login')
        else:
            messages.error(request,"password not matched")
            return redirect('register')
    data = {
            'blood_group':blood_group ,
            'gender_group':gender_group
            
        }
    
    return render(request, 'accounts/register.html' , data )



def logout_user(request):
    logout(request)
    messages.success(request,"loged out successfully")
    return redirect('home')
    