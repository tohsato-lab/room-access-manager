# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime
import json
from pathlib import Path

log_dir = "./log/"


# 年月日
def nowday():
    dt_now = datetime.datetime.now()
    year = str(dt_now.year)
    month = str(dt_now.month)
    month = month.zfill(2)
    day = str(dt_now.day)
    day = day.zfill(2)
    filename = ("%s%s%s" % (year, month, day))

    return filename


# 入出時
def enter_file(student_id, name, time, filename):
    time_list = [time]

    key1 = ['name', 'time']
    value1 = [name, time_list]
    dic1 = {k: v for k, v in zip(key1, value1)}

    dic2 = {"%s" % student_id: dic1}
    print(dic2)
    st = json.dumps(dic2, ensure_ascii=False)

    f = open(Path(log_dir).joinpath('{}.txt'.format(filename)), 'w', encoding="utf_8")
    f.write(st)
    f.close()


# 退出時
def exit_file(student_id, name, time, filename):
    # load file
    load_data: dict = eval(open(Path(log_dir).joinpath('{}.txt'.format(filename)), encoding="utf_8").read())

    if "%s" % student_id in load_data.keys():
        # 更新
        print(type(load_data["%s" % student_id]["time"]))
        # 【仕様追加】最新の時間に置き換える
        if len(load_data["%s" % student_id]["time"]) == 1:
            load_data["%s" % student_id]["time"].append(time)
        else:
            load_data["%s" % student_id]["time"][-1] = time
    else:
        time_list = [time]
        key1 = ['name', 'time']
        value1 = [name, time_list]
        dic1 = {k: v for k, v in zip(key1, value1)}
        load_data.setdefault("%s" % student_id, dic1)

    # write file
    print(load_data)
    with open(Path(log_dir).joinpath('{}.txt'.format(filename)), 'w', encoding="utf_8") as fout:
        fout.write(repr(load_data))


def make_text(student_id, name, time):
    filename = nowday()

    # ファイルが有無の条件分岐
    if Path(log_dir).joinpath('{}.txt'.format(filename)).exists():
        exit_file(student_id, name, time, filename)
    else:
        enter_file(student_id, name, time, filename)
