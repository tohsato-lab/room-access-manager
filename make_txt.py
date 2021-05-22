# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import json
import datetime
import os

#年月日
def nowday():
    
    dt_now = datetime.datetime.now()
    year = str(dt_now.year)
    month = str(dt_now.month)
    month = month.zfill(2)
    day = str(dt_now.day)
    day = day.zfill(2)
    filename=("%s%s%s"%(year,month,day))
    
    return filename

#入出時
def enter_file(student_id ,name ,time, filename):
    
    time_list = []
    time_list.append(time)
    
    key1 = ['name','time']
    value1 = [name, time_list] 
    dic1 = {k: v for k, v in zip(key1, value1)}
    
    
    dic2 = {"%s"%(student_id): dic1}
    print(dic2)
    st = json.dumps(dic2, ensure_ascii=False)
    
    f = open('%s.txt'%(filename), 'w',  encoding="utf_8")
    f.write(st)
    f.close()
    

#退出時
def exit_file(student_id, time, filename):
    #load file
    load_data = eval(open('%s.txt'%(filename),encoding="utf_8").read())
    
    if "%s"%(student_id) in load_data.keys():       
        #更新
        print(type(load_data["%s"%(student_id)]["time"]))
        if len(load_data["%s"%(student_id)]["time"]) < 2:
            load_data["%s"%(student_id)]["time"].append(time)
        print(load_data)
        #write file
        
        with open('%s.txt'%(filename), 'w', encoding="utf_8") as fout:
             fout.write(repr(load_data))
        del load_data


#仮の入力データ
student_id = 26001700234
name = "イケダナオキ"
time = "10:00"

filename = nowday()

#ファイルが有無の条件分岐
if os.path.exists('%s.txt'%(filename)):
    exit_file(student_id, time, filename)
else:
    enter_file(student_id ,name ,time, filename)

