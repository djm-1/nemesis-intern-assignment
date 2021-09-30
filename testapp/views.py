from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib import auth
#from .forms import RegisterForm


# Create your views here.
def alluser(request):
    users=UserProfile.objects.all()

    if request.method=="POST":
        id=request.POST.get('id')
        username=request.POST.get('username')
        address=request.POST.get('addr')
        email=request.POST.get('email')
        
        user=User.objects.get(id=id)
        user.email=email
        user.username=username

        userprofile=UserProfile.objects.get(user__id=id)
        userprofile.address=address

        user.save()
        userprofile.save()
        return HttpResponseRedirect('/')

    else:    
        return render(request,'alluser.html',{'users':users})

def deleteuser(request,id):
    user=UserProfile.objects.get(user__id=id)
    user.delete()
    return HttpResponseRedirect('/')

def signup(request):
    if request.method=="POST":
        if 'username_login' in request.POST:
            user = auth.authenticate(username=request.POST['username_login'],password = request.POST['password_login'])
            if user is not None:
                auth.login(request,user)
                return render (request,'signup.html', {'success':'Signed in as '+ user.username})
            else:
                return render (request,'signup.html', {'error':'Username or password is incorrect!'})            
        
        if 'username' in request.POST:
            if request.POST['password1'] == request.POST['password2']:
                
                user1=User.objects.filter(username = request.POST['username'])
                user2=User.objects.filter(email = request.POST['email'])
                if user1.count()!=0:    
                    return render (request,'signup.html', {'error':'Username is already taken!'})
                
                if user2.count()!=0:    
                    return render (request,'signup.html', {'error':'Email is already in use!'})

                
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
                auth.login(request,user)
                user_profile=UserProfile(
                    user=user,
                    address=request.POST['addr']
                )
                user_profile.save()
                return render (request,'signup.html', {'success':'Signed in as '+ user.username})
            else:
                return render (request,'signup.html', {'error':'Passwords are not matching!'})
    else:
        return render(request,'signup.html')
