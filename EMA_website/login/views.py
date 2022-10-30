from django.shortcuts import render, redirect
from . import models

def index(request):
    
    return render(request, "./login/index.html")

def login(request):
    if request.session.get('loginFlag', None):
        return redirect("/")
    
    if request.method == "POST":
        email = request.POST.get('email', None)
        pwd = request.POST.get('password', None)
        
        if email and pwd:
            user = models.User.objects.filter(email = email)
            
            if user:
                _pwd = user[0].pwd
            else:
                args = {
                    'message' : '您尚未註冊。',
                }
                return render(request, "./login/login.html",args)
            
            if pwd == _pwd:
                request.session['loginFlag'] = True     #把登入狀態改成 True
                request.session['username'] = user[0].name  #設定使用者名稱
                return redirect("/")
            else:
                args = {
                    'message' : '密碼輸入錯誤, 請再試一次',
                }
                return render(request, "./login/login.html",args)
                
    
    return render(request, "./login/login.html")

def register(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        name = request.POST.get('name', None)
        pwd1 = request.POST.get('password 1', None)
        pwd2 = request.POST.get('password 2', None)
        
        if pwd1 == pwd2 :
            user = models.User.objects.filter(email = email)    # 從資料庫查找用戶的資料
            
            if user:
                print("帳戶已經被註冊，請重新註冊。")
                return redirect('/register/')
            new_user = models.User.objects.create()
            new_user.email = email
            new_user.name = name
            new_user.pwd = pwd1
            
            new_user.save()  
            return redirect('/login/')
            
    return render(request, "./login/register.html")

def logout(request):
    if request.session.get('loginFlag'):
        request.session.flush()
        return redirect('/login/')
    
    return redirect('/')

# redirect -> 重新導向至特定url