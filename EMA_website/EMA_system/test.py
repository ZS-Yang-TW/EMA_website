# 引入套件
from manim import *
import os
from explanatoryTools import *
from pathlib import Path

# FLAGS 參數設定
FLAGS = f"-v Warning --disable_caching -pqm"
SCENE = "test" # <- Set the Scene name

class test(explanatoryTools):
    def construct(self):
        self.camera.background_color = WHITE
        self.numberLineAdd(1,2, position = (-5,2.5), ans_question_mode=False,font_color=BLACK)
        self.numberLineAdd(1,2, position = (-5,0), max_length= 3 ,font_color=BLACK)
        self.numberLineAdd(1,2,3,4,5, position = (-5,-2.5), max_length= 8 ,color_radom=True, font_color=BLACK)
        self.numberLineAdd(1,2,3)
        self.pause()
       
        #設定命令參數
        
if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}" #獲取本文件的位置
    os.system(f"manim {script_name} {SCENE} {FLAGS}")   #設定命令參數