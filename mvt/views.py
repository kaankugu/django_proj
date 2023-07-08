from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User, Group 
from django.views.generic.edit import CreateView
from mvt.forms import KayitForm
from mvt.models import Comment
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseServerError
import logging


@login_required(login_url="/login")
def home(request):
    return render(request, 'home.html')

@login_required(login_url="/login")
@user_passes_test(lambda u: u.groups.filter(name='admin').exists(), login_url="/404")
def about(request):
    return render(request, 'about.html')

@login_required(login_url="/login")
def project(request):
    return render(request, 'project.html')



def No_page(request):
    return render(request,"404.html")

@login_required(login_url="/login")
def comment_page(request):
    comments = Comment.objects.all()
    return render(request, 'comment.html', {'comments': comments})

def save_comment(request):
    if request.method == 'POST':
        text = request.POST.get('comment')
        comment = Comment(user=request.user, text=text)
        comment.save()
    return redirect('comment_page')

def delete_comment(request, comment_id):
    if request.method == 'POST' and request.user.is_superuser:
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
    return redirect('comment_page')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html', {"next": reverse("home")})

def signup(request):
    
    if request.method == 'POST':
        form = KayitForm(request.POST)
        if form.is_valid():
           
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            is_seller = form.cleaned_data['is_seller']
            
            
            user = User.objects.create_user(username=username, password=password)
            
            if is_seller == 'user':
                group_name = 'user'
            else:
                group_name = 'admin'
                
            group = Group.objects.get(name=group_name)
            group.user_set.add(user)  
            
            messages.success(request, 'Kayıt başarıyla tamamlandı.')
            new_user = authenticate(username=username, password=password)
            login(request, new_user)
            return redirect('home')
        else:
            
            print(form.errors) # eklediğimiz print komutu
    else:
        form = KayitForm()
    
    return render(request, 'signup.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('home')

class CustomRegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
