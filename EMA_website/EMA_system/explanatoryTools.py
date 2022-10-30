from manim import *
import random
from decimal import Decimal

class explanatoryTools(Scene):
    def numberLineAdd(
        self,
        *args,
        position = (0,0),
        max_length = 10,
        stroke_width = 7,
        label_active = True,
        ans_question_mode = True,
        color_radom = False,
        font_color = WHITE,
        run_time = [],
        **kwargs):
        """Require run_time [n+1]

        Args:
            run_time (_type_): _description_
            position (tuple, optional): _description_. Defaults to (0,0).
            max_length (int, optional): _description_. Defaults to 10.
            stroke_width (int, optional): _description_. Defaults to 7.
            label_active (bool, optional): _description_. Defaults to True.
            ans_question_mode (bool, optional): _description_. Defaults to True.
            font_color (_type_, optional): _description_. Defaults to WHITE.

        Returns:
            _type_: _description_
        """

        # Calculate
        args_decimal = [Decimal(str(num)) for num in args]
        args_str = ["{:g}".format(float(Decimal(str(num)))) for num in args]
        total = float(Decimal(sum(args_decimal)))
        total_str = "{:g}".format(float(Decimal(sum(args))))
        
        # Style settings
        
        color_setting_1 = [RED_A,GREEN_A,BLUE_B,TEAL_B,YELLOW_B,MAROON_A,PURPLE_A]
        color_setting_2 = [BLUE_B]
        color = color_setting_1 if color_radom==True else color_setting_2
        
        lineGroup = [self.numberLine(num,total,random.choice(color),max_length,stroke_width) for num in args]
        labelGroup = [Text(num,color = font_color, font="Noto Sans CJK TC Medium").scale(0.7) for num in args_str]
        
        # Position Adjustment
        for i in range(len(args)):
            if i == 0 : 
                lineGroup[i].move_to((RIGHT*position[0]+UP*position[1]),aligned_edge=LEFT)
            else : 
                lineGroup[i].next_to(lineGroup[i-1],RIGHT).shift(LEFT*0.25)
                
            labelGroup[i].next_to(lineGroup[i],DOWN)
        
        sumLine = Line(lineGroup[0].get_left(), lineGroup[len(args)-1].get_right()).set_color(ORANGE)
        sumBrace = Brace(sumLine, direction = UP, sharpness = 0.5, color=font_color)
        sumText = Text(total_str,color = font_color, font="Noto Sans CJK TC Medium").scale(0.7).next_to(sumBrace, direction = UP)
        questionText = Text("？",color = font_color, font="Noto Sans CJK TC Medium").scale(0.7).next_to(sumBrace, direction = UP)
        
        # Animation
        if (run_time == []):
            run_time = [1 for time in range(len(args)+1)]
            
        for i in range(len(args)):
            self.play(Create(lineGroup[i]),Write(labelGroup[i]),run_time = run_time[i])
            
        if (label_active):   
            if (ans_question_mode): self.play(Write(sumBrace),Write(sumText),run_time = run_time[-1])
            else : self.play(Write(sumBrace),Write(questionText),run_time = run_time[-1])
                
                
        return total
        
    def numberLine(self,num,total,color,max_length,stroke_width=5):
        line = NumberLine(
            x_range=[0, num, num],
            color = color,
            stroke_width = stroke_width,
            length = max_length*num/total,
        )
        
        return line   