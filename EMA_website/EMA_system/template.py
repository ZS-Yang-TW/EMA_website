from manim import *
from calculate import *

class addition(Scene):
    def object_plus_number(self,OBJECT,NUM):  

        #寫題目
        text = Text(f"+{NUM}")
        
        #位置設定(放在物件右邊)
        text.next_to(OBJECT,RIGHT*0.5)
        
        #縮放
        
        #影像寫入
        self.play(Write(text),run_time=0.1)
        
        return text
    
    def plus_number(self,NUM,POS):  

        #寫題目
        text = Text(f"+{NUM}")
        
        #位置設定
        x_pos = RIGHT*POS[0]
        y_pos = UP*POS[1]
        text.move_to(x_pos+y_pos)
        
        #縮放
        
        #影像寫入
        self.play(Write(text),run_time=1)
        
        return text
    
    def muti_addition(self,NUM_LIST,POS):  

        #寫題目
        text = Text(f"{NUM_LIST[0]}")
        
        #位置設定
        x_pos = RIGHT*POS[0]
        y_pos = UP*POS[1]
        text.move_to(x_pos+y_pos)
        self.play(Write(text),run_time=0.1)

        for i in range(len(NUM_LIST)-1):
            text = self.object_plus_number(text,NUM_LIST[i+1])
            if (i == (len(NUM_LIST)-2) ):
                equal = Text("= ?").next_to(text)
                self.play(Write(equal))
                
        #縮放
        #影像寫入
        
    def addition_table(self,NUM,POS,SCALE):
        #輸入數字
        a = NUM[0]
        b = NUM[1]
        
        #計算各位數，並轉成整數、字串型態
        a_str_list, b_str_list, ans_str_list, sum_str_list, carry_str_list = calculate_str(a,b)
        
        #計算答案
        Ans = a+b
  
        #位置表
        t0 = Table(
            [[a_str_list[3], a_str_list[2], a_str_list[1], a_str_list[0]],
            [b_str_list[3], b_str_list[2], b_str_list[1], b_str_list[0]],
            [" "," "," "," "]],
            row_labels=[Text(" "), Text("+"), Text("=")],
            col_labels=[Text("千"), Text("百"), Text("十"), Text("個")],
            include_outer_lines=True)
        
        for i in range(4):
            t0.add_highlighted_cell((1,2+i), color=GREEN)
            
        x_pos = RIGHT*POS[0]
        y_pos = UP*POS[1]
        t0.scale(SCALE)
        t0.move_to(x_pos+y_pos)
        
        #關注位數
        attention = []
        for i in range(4):
            attention.append(t0.get_cell((4,5-i), color=RED))
        
        #將答案轉成轉成轉成Text()型態
        Ans_Text_list = []
        for i in range(4):
            Ans_Text_list.append(Text(ans_str_list[i]).scale(SCALE).move_to(t0.get_cell((4,5-i))))
        
        #將進位轉成Text()
        carry_Text_list = []
        for i in range(3):
            carry_Text_list.append(Text(carry_str_list[i+1],color = YELLOW,stroke_width=0.2).scale(SCALE*0.8).move_to(t0.get_cell((4,4-i))).shift(UP*0.11+RIGHT*0.3))
        
        #等待時間
        waiting_time =[1,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,2]
        
        #--影格生成--#
        
        #生成表格
        self.play(Create(t0))
        self.wait(waiting_time[3])
        
        #直式加法過程
        for i in range(4):
            self.play(Create(attention[i]))
            self.wait(waiting_time[(4+i*3)])
            
            self.play(Write(Ans_Text_list[i]))
            self.wait(waiting_time[(5+i*3)])
            
            if (i!=3):
                self.play(Write(carry_Text_list[i]))
            self.play(Uncreate(attention[i]))
            self.wait(waiting_time[(6+i*3)])
            
        return Ans
    
    def table_gen(self, a_str_list, b_str_list, ans_str_list, max_len):
    
        #column標籤
        col_name_ref=[Text('千兆'), Text('百兆'), Text('十兆'), Text('兆'), Text('千億'), Text('百億'), Text('十億'), Text('億'), Text('千萬'), Text('百萬'), Text('十萬'), Text('萬'), Text('千'), Text('百'), Text('十'), Text('個')]
        col_name = col_name_ref[-max_len:]

        #產生位置表
        t0 = Table(
            [a_str_list, b_str_list, ans_str_list],
            row_labels=[Text(" "), Text("+"), Text("=")],
            col_labels = col_name,
            include_outer_lines=True)

        #尺寸調整
        scale_x = (config.frame_width-2)/t0.width
        scale_y = (config.frame_height-5)/t0.height

        t0 = t0.scale(min(scale_x, scale_y)).to_corner(DOWN, buff=1.6)

        #顏色調整
        for i in range(max_len):
                t0.add_highlighted_cell((1,2+i), color=GREEN)
        t0.get_horizontal_lines()[4].set_color(GREEN)
        t0.get_entries_without_labels()[-max_len:].set_color(BLACK)

        return t0