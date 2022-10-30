from manim import *
from pathlib import Path
from calculate import *
from addition_text_output import *
from voicetools import voice_tools
from template import *
from explanatoryTools import explanatoryTools
import time


# FLAGS 參數設定
FLAGS = f"-v Warning --disable_caching -pqm"
SCENE = "EMA_output" # <- Set the Scene name

# ——————————— 模板製作區塊 ——————————— # 
class EMA_output(addition, explanatoryTools):
    def construct(self):
        # 輸入數字
        a = 1978
        b = 1579
        start_time = time.time()
        
        # 計算各位數，並轉成整數、字串型態
        a_str_list, b_str_list, ans_str_list, carry_str_list, max_len = calculate_str(a,b)
        
        # 計算答案
        Ans = a+b
        Ans_text = Text(f"答案是:{Ans}").to_corner(DR)
        
        # 寫題目
        question_text = Text(f"{a} + {b} = ?")
        question_text.to_corner(UP,buff=0.5)
        
        # 位置表
        t0 = self.table_gen(a_str_list, b_str_list, ans_str_list, max_len)
        
        # 關注位數
        attention = []
        for i in range(max_len):
            attention.append(t0.get_cell((4, max_len+1-i), color=RED))
       
       # 將答案轉成轉成轉成Text()型態
        Ans_Text_list = []
        for i in range(4):
            Ans_Text_list.append(Text(ans_str_list[i]).scale(0.5).move_to(t0.get_cell((4,5-i))))
       
        # 將進位轉成Text()
        carry_Text_list = []
        
        for i in range(max_len):
            carry_Text_list.append(Text(carry_str_list[i], color = YELLOW, stroke_width=0.2).scale(0.4).next_to(t0.get_cell((3, max_len+1-i)), DL*0.5))
        
        #---------- 模板輸出區域 ---------- #
        # 輸出詳解文本
        text_output(a,b)
        
        # 輸出音檔
        addition_voice = voice_tools()
        addition_voice.voice_generate('text_output.txt')
        
        time_line = addition_voice.voice_time.get_time_line()
        addition_voice.voice_time.set_run_wait_ratio(1)
        interval_time = addition_voice.voice_time.get_interval_time()
        run_time = addition_voice.voice_time.get_run_time()
        wait_time = addition_voice.voice_time.get_wait_time()
        print(time_line)
        print(interval_time)
        
        
        # 影音對齊
        self.add_sound("voice_output.mp3")
        
        # 算式
        self.add(question_text)
        
        # 數線
        self.numberLineAdd(a, b, position = (-3,1.5), max_length = 6, ans_question_mode=False,run_time = run_time[0:3])
        self.wait(run_time[3])
        self.play(Create(t0),run_time=run_time[4])
        self.wait(run_time[5])
        
        # 直式加法過程
        for i in range(max_len):
            self.play(Create(attention[i]), run_time = run_time[6+7*i])
            self.wait(run_time[7+7*i])
            
            self.play(Write(t0.get_entries_without_labels((3,4-i)).set_color(WHITE)), run_time = run_time[8+7*i])
            self.wait(run_time[9+7*i])
            
            if (i != 3):
                self.play(Write(carry_Text_list[i]), run_time = run_time[10+7*i])
                self.wait(run_time[11+7*i])
                self.play(Uncreate(attention[i]), run_time = run_time[12+7*i])
                
            else : self.play(Uncreate(attention[i]))
        
        # 寫答案
        self.play(AddTextLetterByLetter(Ans_text))
        self.wait(3)
        
        #---------- 模板輸出區域 ---------- #
# ——————————— 模板製作區塊 ——————————— # 

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}" #獲取本文件的位置
    os.system(f"manim {script_name} {SCENE} {FLAGS}")   #設定命令參數