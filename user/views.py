from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def userRegister(request):
    if request.method == 'POST':
        kullaniciAdi=request.POST['kullanici']
        email=request.POST['email']
        sifre1=request.POST['sifre1']
        sifre2=request.POST['sifre2']

        if sifre1==sifre2:
            #kullanıcı adının kullanılıp kullanılmadığını kontrol eder
            if User.objects.filter(username=kullaniciAdi).exists():
                messages.warning(request, 'Kullanıcı adı zaten mevcut.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email kullanımda.')
                return redirect('register')
            elif len(sifre1)<6:
                messages.warning(request, 'Şifre en az 6 karakterden oluşmalı.')
                return redirect('register')
            elif kullaniciAdi.lower() in sifre1:
                messages.warning(request, 'Şifre ile kullanıcı adı benzer olmamalıdır.')
                return redirect('register')
            else:
                #kullaıcı kayıt işleme
                user= User.objects.create_user(
                    username=kullaniciAdi,
                    email=email,
                    password=sifre1
                )
                user.save()
                messages.success(request, 'Kullanıcı oluşturuldu')
                return redirect('login')
        else:
            messages.warning(request, 'Şifreler uyuşmuyor!')
            return redirect('register')
    return render(request, 'user/register.html')

def userLogin(request):
    if request.method == 'POST':
        kullanici= request.POST['kullaniciAdi']
        sifre= request.POST['sifre']

        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş Yapıldı.')
            return redirect('index')
        else:
            messages.warning(request, 'Kullanıcı adı veya şifre hatalı!')
            return redirect('login')
    return render(request, 'user/login.html')

def userLogout(request):
    logout(request)
    messages.success(request,'Çıkış yaptınız.')
    return redirect('index')

