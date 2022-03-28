from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Blog, ContactDetails
from .forms import SignUpform,AddBlogForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.models import Group, User

# Create your views here.
def base(request):
    return render(request,'base.html')

def home(request):
    fm = Blog.objects.all()
    return render(request,'home.html',{'fm':fm})

def about(request):
    return render(request,'about.html')

class User_signup(View):
    def get(self,request):
        fm = SignUpform()
        return render(request,'signup.html',{'fm':fm})

    def post(self,request):
        fm = SignUpform(request.POST or None)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Success!! Account created Successfully.")
        else:
            messages.warning(request,'Error! Something went wrong, Try Again')
        return render(request, 'signup.html', {'fm': fm})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phoneno']
        state = request.POST['state']
        city = request.POST['city']
        fm = ContactDetails(name=name,email=email,address=address,phoneno=phone,state=state,city=city)
        fm.save()
        messages.success(request, "Success!! We will contact Soon.")
    return render(request, 'contact.html')

def addblog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = AddBlogForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Success!! Your Blog is Posted Successfully. ")
        else:
            fm = AddBlogForm()
        return render(request,'addblog.html')
    else:
        return redirect('/login')

def dashboard(request):
        users = Blog.objects.all()
        user = request.user
        fullname = user.get_full_name()
        grp = user.groups.all()
        author = Blog.objects.filter(user=request.user)
        return render(request,'dashboard.html',{'users':users, 'fullname':fullname, 'grp':grp})

def delete(request,id):
    user = Blog.objects.filter(id=id).delete()
    return redirect('/dashboard')

def edit(request,id):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user = Blog.objects.filter(id=id)
            user.title = request.POST.get('title')
            user.content = request.POST.get('content')
            user.author = request.POST.get('author')
        return redirect('/dashboard')
    else:
        return redirect('/login')

def details(request,id):
    blog_id = Blog.objects.filter(id=id)
    return render(request,'details.html',{'blog_id':blog_id})
