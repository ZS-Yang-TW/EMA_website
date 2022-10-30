from calculate import calculate,calculate_str

def text_output (a,b):
    a_int_list, b_int_list, ans_int_list, carry_int_list = calculate(a,b)
    a_str_list, b_str_list, ans_str_list, carry_str_list, max_len = calculate_str(a,b)
    
    lines = [f"<speak version=\"1.0\" xmlns=\"http://www.w3.org/2001/10/synthesis\" xml:lang=\"zh-TW\">\n",
            f"    <voice name=\"zh-TW-YunJheNeural\">\n",
            f"    <prosody rate=\"-10.00%\">\n",
            
            #-- Add Eplanation at Here "Type: f"        [Eplanation]\n" --#
            # "Bookmark type" :<bookmark mark=\'mark_N\'/>，please put after the character.
            
            f"        <bookmark mark=\'mark_0\'/>{a}，<bookmark mark=\'mark_1\'/>加上{b}，<bookmark mark=\'mark_2\'/>河起來會是多少呢?<bookmark mark=\'mark_3\'/>\n",
            f"        算加法，我們可以利用位置表來幫助我們做對位。<bookmark mark=\'mark_4\'/>\n",
            f"        我有<bookmark mark=\'mark_5\'/>{a_int_list[3]}千、{a_int_list[2]}百、{a_int_list[1]}十、{a_int_list[0]}。加上{b_int_list[3]}千、{b_int_list[2]}百、{b_int_list[1]}十、{b_int_list[0]}。\n",
            f"        對位對好了，從最右邊開始計算。<bookmark mark=\'mark_6\'/>\n",
            
            f"        首先，<bookmark mark=\'mark_7\'/>\n",
            f"        {a_int_list[0]}個1,，加{b_int_list[0]}個1。\n",
            f"        {a_int_list[0]}加{b_int_list[0]}，等於{a_int_list[0]+b_int_list[0]}。\n",
            f"        {a_int_list[0]+b_int_list[0]}個1，先<bookmark mark=\'mark_8\'/>\n",
            f"        把{ans_int_list[0]}寫下來。<bookmark mark=\'mark_9\'/>\n",
            f"        那{a_int_list[0]+b_int_list[0]}個1當中，每十個1，會等於1個十。所以<bookmark mark=\'mark_10\'/>\n",
            f"        進位{carry_int_list[0]}<bookmark mark=\'mark_11\'/>\n",
            f"        個十過來。<bookmark mark=\'mark_12\'/>\n",
            
            f"        再來，<bookmark mark=\'mark_13\'/>\n",
            f"        十位的計算<bookmark mark=\'mark_14\'/>。\n",
            f"        {a_int_list[1]}個十,，加{b_int_list[1]}個十。\n",
            f"        {a_int_list[1]}加{b_int_list[1]}，等於{a_int_list[1]+b_int_list[1]}。\n",
            f"        {a_int_list[1]+b_int_list[1]}再加上剛剛進位的{carry_int_list[0]}。\n",
            f"        {a_int_list[1]+b_int_list[1]}加{carry_int_list[0]}，等於{a_int_list[1]+b_int_list[1]+carry_int_list[0]}。\n",
            f"        {a_int_list[1]+b_int_list[1]+carry_int_list[0]}個十，先<bookmark mark=\'mark_15\'/>\n",
            f"        把{ans_int_list[1]}寫下來。<bookmark mark=\'mark_16\'/>\n",
            f"        那{a_int_list[1]+b_int_list[1]+carry_int_list[0]}個十當中，每十個十，會等於1個百。所以<bookmark mark=\'mark_17\'/>\n",
            f"        進位{carry_int_list[1]}<bookmark mark=\'mark_18\'/>\n",
            f"        個十過來。<bookmark mark=\'mark_19\'/>\n",
            
            f"        再來，<bookmark mark=\'mark_20\'/>\n",
            f"        百位的計算<bookmark mark=\'mark_21\'/>。\n",
            f"        {a_int_list[2]}個百,，加{b_int_list[2]}個百。\n",
            f"        {a_int_list[2]}加{b_int_list[2]}，等於{a_int_list[2]+b_int_list[2]}。\n",
            f"        {a_int_list[2]+b_int_list[2]}再加上剛剛進位的{carry_int_list[1]}。\n",
            f"        {a_int_list[2]+b_int_list[2]}加{carry_int_list[2]}，等於{a_int_list[2]+b_int_list[2]+carry_int_list[1]}。\n",
            f"        {a_int_list[2]+b_int_list[2]+carry_int_list[1]}個百，先<bookmark mark=\'mark_22\'/>\n",
            f"        把{ans_int_list[2]}寫下來。<bookmark mark=\'mark_23\'/>\n",
            f"        那{a_int_list[2]+b_int_list[2]+carry_int_list[1]}個百當中，每十個百，會等於1個千。所以<bookmark mark=\'mark_24\'/>\n",
            f"        進位{carry_int_list[2]}<bookmark mark=\'mark_25\'/>\n",
            f"        個千過來。<bookmark mark=\'mark_26\'/>\n",
            
            f"        最後，<bookmark mark=\'mark_27\'/>\n",
            f"        千位的計算<bookmark mark=\'mark_28\'/>。\n",
            f"        {a_int_list[3]}個千,，加{b_int_list[3]}個千。\n",
            f"        {a_int_list[3]}加{b_int_list[3]}，等於{a_int_list[3]+b_int_list[3]}。\n",
            f"        {a_int_list[3]+b_int_list[3]}再加上剛剛進位的{carry_int_list[2]}。\n",
            f"        {a_int_list[3]+b_int_list[3]}加{carry_int_list[2]}，等於{a_int_list[3]+b_int_list[3]+carry_int_list[2]}。\n",
            f"        {a_int_list[3]+b_int_list[3]+carry_int_list[2]}個千，我們<bookmark mark=\'mark_29\'/>\n"
            f"        擺在千位。<bookmark mark=\'mark_30\'/>\n"
    
            f"        所以，<bookmark mark=\'mark_31\'/>這一題的答案是{a+b}。\n"
            
            
            #-- End Eplanation --#
            
            f"    </prosody>\n",
            f"    </voice>\n",
            f"</speak>\n",
            ]
    
    path = "text_output.txt"
    with open(path, 'w', encoding='utf-8') as f:    # 注意使用 UTF-8 編碼
        f.writelines(lines)

if __name__ == '__main__':
    text_output(1987,1579)