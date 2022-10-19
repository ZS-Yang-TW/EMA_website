import email
from django.shortcuts import render
from .models import TB_1
# Create your views here.
def index(request):
    # Login Session
    request.session['isLogin'] = False
    
    # Form Function
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        
        if name and age:
            print(name, age)
        
        obj = TB_1.objects.create(name = name, age = age, type = '0')
        obj.save()
    # TODO
    user_data = TB_1.objects.get(name='Adam')
    arg = {
        'name' : 'Steven',
        'age' : 23,
        'VIP_valid' : 'True',
        'dict' : {
            'a' : 10,
            'b' : 20,
        },
        'loops' : [1,2,3,4,5],
        'test' : {
            'test1' : 'test1',
            'test2' : 'test2',
        },
        'user_data' : user_data,
    }
    return render(request, './polls/index.html', arg)