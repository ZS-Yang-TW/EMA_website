from django.shortcuts import render
from login import models
import os
import csv
GENERATE_PATH = "C:/Users/msyco/桌面/EMA_web/EMA_website/EMA_generate.py"

# Create your views here.
def index(request):
    return render(request, './ema/ema.html')

def generate_EMA(request):
    question_input = '尚未輸入'
    now_user_name = 'None'
    if request.method == 'POST':
        question_input = request.POST.get('question', None)
        now_user_name = request.session.get('username',None)
        
        user_data = models.User.objects.get(name = now_user_name)
        user_data.question = question_input
        user_data.save()
        print(user_data.question)

        if question_input:
            os.system(f"python {GENERATE_PATH}")
            
    args = {
        'question' : question_input,
    }
    
    # 開啟輸出的 CSV 檔案
    with open('output.csv', 'w', newline='') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)

        # 寫入一列資料
        writer.writerow([now_user_name])
    
    return render(request, './ema/index.html',args)