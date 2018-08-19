import os

def readini(path):
    if os.path.exists(path):
        try:
            a = open(path,encoding='utf-8')
            vali_key = a.readline().replace('\n','')
        except:
            a = open(path,encoding='gbk')
            vali_key = a.readline().replace('\n','')
        if vali_key == "*A3F74A1BC90980D5*":
            ini_list = a.readlines()
            ini_list = [ini.replace("\n",'') for ini in ini_list]
            if len(ini_list) == 1:
                rule_list = ini_list[0].split(':')[1].split('|')
                a.close()
                return rule_list
            else:
                a.close()
                return ini_list



def readtxtfile(path):
    # if not os.path.exists(path):
    #     return 0
    # else:
    try:
        with open(path,encoding='utf-8') as a:
            txt = a.read()
    except:
        with open(path,encoding='gbk') as a:
            txt = a.read()
    return txt
