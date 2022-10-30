import os

# Django Setting
PROJECT_NAME = 'EMA_website'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%s.settings' % PROJECT_NAME)
import django
django.setup()

# EMA system setting
from manim import *
from EMA_system.explanatoryTools import explanatoryTools
from pathlib import Path

FLAGS = f"-v Warning --media_dir C:/Users/msyco/桌面/EMA_web/EMA_website/static --disable_caching -qm"
SCENE = "output" # <- Set the Scene name

# app models
from login import models
import csv

# 讀取現在使用者
with open('output.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    column = [row[0] for row in rows]
name = column[0]
muser = models.User.objects.get(name = name)

class output(explanatoryTools): 
    def construct(self):
        num = muser.question.split('+')
        print(num[0],num[1])
        self.camera.background_color = WHITE
        self.numberLineAdd(int(num[0]),int(num[1]), position = (-5,2.5), ans_question_mode=False,font_color=BLACK)
        self.pause()

def main():
    script_name = f"{Path(__file__).resolve()}" #獲取本文件的位置
    os.system(f"manim {script_name} {SCENE} {FLAGS}")   #設定命令參數

if __name__ == '__main__':
    main()