from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time
from datetime import datetime, timedelta
import threading
import os
import sqlite3
import subprocess
import codecs
#import RPi.GPIO as GPIO
import xlwt
import xlrd
import codecs
import bluetooth
import serial
import math
import pexpect
#from pexpect import spawn
# import PyOBEX
# from PyOBEX import ObexFTP
# import obexftp
# from PyOBEX.client import Client
# import fabric
# from fabric import operations


machine_number = 'B0508'


root = tk.Tk()
root.geometry("800x600")

# read local date、time


def date_read():
    date = datetime.now().strftime('%Y-%m-%d')
    return date


def time_read():
    todaytime = datetime.now().strftime('%H:%M:%S')
    return todaytime


# 初始參數區
inputtxt = 0
printtype = 0
year = 0
month = 0
date = 0
hour = 0
minute = 0
year1 = 0
month1 = 0
date1 = 0
hour1 = 0
minute1 = 0
year11 = 0
month11 = 0
date11 = 0
hour11 = 0
minute11 = 0
calibration = 0
calibratecheck = 0
searchid = "输入病人ID"
qrcode = 0
qrcheck = 0
searchdate = "输入测试日期 (yyyymmdd) \n or (yyyymm)"
show_number = 0
font_number = 0
channel = 0
todaytime = 0

input_text = ''
space1 = ''
space2 = ''
# selplace = tk.StringVar(root)
# selplace.set(" ")
# show_date=tk.StringVar(root)
# show_date.set(" ")
# print_title = tk.StringVar(root)
# print_title.set(" ")
load = None
loading2 = None
runcal = None
alarm = None
alarm1 = None
alarm2 = None
alarm_number = 0
alarm_count = 0
in_voltage = ''
isuppercase = 0
value_current = None
count_list = [0] * 9
count_list_en = [0] * 8
values = tk.StringVar(root)
values.set(" ")
last_command = -1
Hb_data = 0
HbA1c_data = 0
t1 ='請掃描包裝袋上的QR code，\n以決定檢測品項。'

img001 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/logo.png'
photo001 = ImageTk.PhotoImage(Image.open(img001))
img002 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/file.png'
photo002 = ImageTk.PhotoImage(Image.open(img002))
img003 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/test.png'
photo003 = ImageTk.PhotoImage(Image.open(img003))
img004 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/setup.png'
photo004 = ImageTk.PhotoImage(Image.open(img004))
img005 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/home.png'
photo005 = ImageTk.PhotoImage(Image.open(img005))
img006 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/back.png'
photo006 = ImageTk.PhotoImage(Image.open(img006))
img007 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/settime.png'
photo007 = ImageTk.PhotoImage(Image.open(img007))
img008 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/setposition.png'
photo008 = ImageTk.PhotoImage(Image.open(img008))
img009 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/update.png'
photo009 = ImageTk.PhotoImage(Image.open(img009))
img010 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/save.png'
photo010 = ImageTk.PhotoImage(Image.open(img010))
img011 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/confirm.png'
photo011 = ImageTk.PhotoImage(Image.open(img011))
img012 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/calibration.png'
photo012 = ImageTk.PhotoImage(Image.open(img012))
img013 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/startdetect.png'
photo013 = ImageTk.PhotoImage(Image.open(img013))

img015 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/print.png'
photo015 = ImageTk.PhotoImage(Image.open(img015))
img016 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/left.png'
photo016 = ImageTk.PhotoImage(Image.open(img016))
img017 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/right.png'
photo017 = ImageTk.PhotoImage(Image.open(img017))

img019 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/export.png'
photo019 = ImageTk.PhotoImage(Image.open(img019))

img024 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/lastpage.png'
photo024 = ImageTk.PhotoImage(Image.open(img024))
img025 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/nextpage.png'
photo025 = ImageTk.PhotoImage(Image.open(img025))
img026 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/confirm2.png'
photo026 = ImageTk.PhotoImage(Image.open(img026))
img027 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/bluetooth.png'
photo027 = ImageTk.PhotoImage(Image.open(img027))
img028 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/search.png'
photo028 = ImageTk.PhotoImage(Image.open(img028))
img029 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/pair.png'
photo029 = ImageTk.PhotoImage(Image.open(img029))
img030 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/enterY.png'
photo030 = ImageTk.PhotoImage(Image.open(img030))
img031 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/enterMon.png'
photo031 = ImageTk.PhotoImage(Image.open(img031))
img032 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/enterD.png'
photo032 = ImageTk.PhotoImage(Image.open(img032))
img033 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/enterH.png'
photo033 = ImageTk.PhotoImage(Image.open(img033))
img034 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/enterMin.png'
photo034 = ImageTk.PhotoImage(Image.open(img034))
img035 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/ID.png'
photo035 = ImageTk.PhotoImage(Image.open(img035))


img041 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/home1.png'
photo041 = ImageTk.PhotoImage(Image.open(img041))
img042 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/back1.png'
photo042 = ImageTk.PhotoImage(Image.open(img042))
img043 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/settime1.png'
photo043 = ImageTk.PhotoImage(Image.open(img043))
img044 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/setposition1.png'
photo044 = ImageTk.PhotoImage(Image.open(img044))
img045 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/update1.png'
photo045 = ImageTk.PhotoImage(Image.open(img045))
img046 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/save1.png'
photo046 = ImageTk.PhotoImage(Image.open(img046))
img047 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/confirm_1.png'
photo047 = ImageTk.PhotoImage(Image.open(img047))
img048 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/calibration1.png'
photo048 = ImageTk.PhotoImage(Image.open(img048))
img049 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/startdetect1.png'
photo049 = ImageTk.PhotoImage(Image.open(img049))

img051 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/print1.png'
photo051 = ImageTk.PhotoImage(Image.open(img051))
img052 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/left1.png'
photo052 = ImageTk.PhotoImage(Image.open(img052))
img053 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/right1.png'
photo053 = ImageTk.PhotoImage(Image.open(img053))

img055 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/export1.png'
photo055 = ImageTk.PhotoImage(Image.open(img055))
img056 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/print1.png'
photo056 = ImageTk.PhotoImage(Image.open(img056))
img057 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/confirm2_1.png'
photo057 = ImageTk.PhotoImage(Image.open(img057))
img058 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/bluetooth1.png'
photo058 = ImageTk.PhotoImage(Image.open(img058))
img059 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/search1.png'
photo059 = ImageTk.PhotoImage(Image.open(img059))
img060 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/pair1.png'
photo060 = ImageTk.PhotoImage(Image.open(img060))
img061 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/enterY1.png'
photo061 = ImageTk.PhotoImage(Image.open(img061))
img062 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/enterMon1.png'
photo062 = ImageTk.PhotoImage(Image.open(img062))
img063 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/enterD1.png'
photo063 = ImageTk.PhotoImage(Image.open(img063))
img064 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/enterH1.png'
photo064 = ImageTk.PhotoImage(Image.open(img064))
img065 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/enterMin1.png'
photo065 = ImageTk.PhotoImage(Image.open(img065))
img066 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/ID1.png'
photo066 = ImageTk.PhotoImage(Image.open(img066))
img067 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/left1.png'
photo067 = ImageTk.PhotoImage(Image.open(img067))
img068 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/right1.png'
photo068 = ImageTk.PhotoImage(Image.open(img068))
img069 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/yes.png'
photo069 = ImageTk.PhotoImage(Image.open(img069))
img070 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/yes1.png'
photo070 = ImageTk.PhotoImage(Image.open(img070))
img071 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/no.png'
photo071 = ImageTk.PhotoImage(Image.open(img071))
img072 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/no1.png'
photo072 = ImageTk.PhotoImage(Image.open(img072))
img111 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/1.png'
photos1 = ImageTk.PhotoImage(Image.open(img111))
img112 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/2.png'
photos2 = ImageTk.PhotoImage(Image.open(img112))
img113 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/3.png'
photos3 = ImageTk.PhotoImage(Image.open(img113))
img114 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/4.png'
photos4 = ImageTk.PhotoImage(Image.open(img114))
img115 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/5.png'
photos5 = ImageTk.PhotoImage(Image.open(img115))
img116 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/6.png'
photos6 = ImageTk.PhotoImage(Image.open(img116))
img117 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/7.png'
photos7 = ImageTk.PhotoImage(Image.open(img117))
img118 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/8.png'
photos8 = ImageTk.PhotoImage(Image.open(img118))
img119 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/9.png'
photos9 = ImageTk.PhotoImage(Image.open(img119))
img120 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/0.png'
photos10 = ImageTk.PhotoImage(Image.open(img120))

img122 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/del.png'
photos12 = ImageTk.PhotoImage(Image.open(img122))
img123 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/En.png'
photos13 = ImageTk.PhotoImage(Image.open(img123))
img124 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/backspace.png'
photos14 = ImageTk.PhotoImage(Image.open(img124))
img125 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/confirm3.png'
photos15 = ImageTk.PhotoImage(Image.open(img125))
img126 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/abc.png'
photos16 = ImageTk.PhotoImage(Image.open(img126))
img127 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/def.png'
photos17 = ImageTk.PhotoImage(Image.open(img127))
img128 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/ghi.png'
photos18 = ImageTk.PhotoImage(Image.open(img128))
img129 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/jkl.png'
photos19 = ImageTk.PhotoImage(Image.open(img129))
img130 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/mno.png'
photos20 = ImageTk.PhotoImage(Image.open(img130))
img131 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/pqrs.png'
photos21 = ImageTk.PhotoImage(Image.open(img131))
img132 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/tuv.png'
photos22 = ImageTk.PhotoImage(Image.open(img132))
img133 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/wxyz.png'
photos23 = ImageTk.PhotoImage(Image.open(img133))
img134 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/shift.png'
photos24 = ImageTk.PhotoImage(Image.open(img134))
img135 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/123.png'
photos25 = ImageTk.PhotoImage(Image.open(img135))
img136 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/en_set.png'
photos26 = ImageTk.PhotoImage(Image.open(img136))
img137 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/space.png'
photos27 = ImageTk.PhotoImage(Image.open(img137))
img138 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/u_ABC.png'
photos28 = ImageTk.PhotoImage(Image.open(img138))
img139 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/u_DEF.png'
photos29 = ImageTk.PhotoImage(Image.open(img139))
img140 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/u_GHI.png'
photos30 = ImageTk.PhotoImage(Image.open(img140))
img141 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/u_JKL.png'
photos31 = ImageTk.PhotoImage(Image.open(img141))
img142 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/u_MNO.png'
photos32 = ImageTk.PhotoImage(Image.open(img142))
img143 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/u_PQRS.png'
photos33 = ImageTk.PhotoImage(Image.open(img143))
img144 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/u_TUV.png'
photos34 = ImageTk.PhotoImage(Image.open(img144))
img145 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/u_WXYZ.png'
photos35 = ImageTk.PhotoImage(Image.open(img145))

img155 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/clearData.png'
photos155 = ImageTk.PhotoImage(Image.open(img155))
img156 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/clearData1.png'
photos156 = ImageTk.PhotoImage(Image.open(img156))
img157 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/more.png'
photos157 = ImageTk.PhotoImage(Image.open(img157))
img158 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/more1.png'
photos158 = ImageTk.PhotoImage(Image.open(img158))
img159 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/cancel.png'
photos159 = ImageTk.PhotoImage(Image.open(img159))
img160 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/cancel1.png'
photos160 = ImageTk.PhotoImage(Image.open(img160))
img146 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/printing.png'
photos36 = ImageTk.PhotoImage(Image.open(img146))
img147 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/removing.png'
photos37 = ImageTk.PhotoImage(Image.open(img147))

img147_ex1 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/exporting1.png'
photos_ex1 = ImageTk.PhotoImage(Image.open(img147_ex1))
img147_ex2 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/exporting2.png'
photos_ex2 = ImageTk.PhotoImage(Image.open(img147_ex2))
img147_ex3 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/exporting3.png'
photos_ex3 = ImageTk.PhotoImage(Image.open(img147_ex3))

img148_cal1 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/caling1.png'
photos_cal1 = ImageTk.PhotoImage(Image.open(img148_cal1))
img148_cal2 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/caling2.png'
photos_cal2 = ImageTk.PhotoImage(Image.open(img148_cal2))
img148_cal3 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/caling3.png'
photos_cal3 = ImageTk.PhotoImage(Image.open(img148_cal3))

img149_test1 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/testing1.png'
photos_test1 = ImageTk.PhotoImage(Image.open(img149_test1))
img149_test2 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/testing2.png'
photos_test2 = ImageTk.PhotoImage(Image.open(img149_test2))
img149_test3 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/testing3.png'
photos_test3 = ImageTk.PhotoImage(Image.open(img149_test3))

img150_QR1 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/QRing1.png'
photos_QR1 = ImageTk.PhotoImage(Image.open(img150_QR1))
img150_QR2 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/QRing2.png'
photos_QR2 = ImageTk.PhotoImage(Image.open(img150_QR2))
img150_QR3 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/QRing3.png'
photos_QR3 = ImageTk.PhotoImage(Image.open(img150_QR3))

img151 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/itemnext.png'
photos151 = ImageTk.PhotoImage(Image.open(img151))
img152 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/itemlast.png'
photos152 = ImageTk.PhotoImage(Image.open(img152))

img161 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/glass.png'
photos161 = ImageTk.PhotoImage(Image.open(img161))
img162 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/glass2.png'
photos162 = ImageTk.PhotoImage(Image.open(img162))
img163 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/glass3.png'
photos163 = ImageTk.PhotoImage(Image.open(img163))
img164 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/glass4.png'
photos164 = ImageTk.PhotoImage(Image.open(img164))

img165 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/bluePrinter.png'
photos165 = ImageTk.PhotoImage(Image.open(img165))
img166 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/bluePrinter1.png'
photos166 = ImageTk.PhotoImage(Image.open(img166))
img167 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/blueStorage.png'
photos167 = ImageTk.PhotoImage(Image.open(img167))
img168 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/blueStorage1.png'
photos168 = ImageTk.PhotoImage(Image.open(img168))
img169 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/DataExport.png'
photos169 = ImageTk.PhotoImage(Image.open(img169))
img170 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/DataExport1.png'
photos170 = ImageTk.PhotoImage(Image.open(img170))

img171 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/FNF.png'
photos171 = ImageTk.PhotoImage(Image.open(img171))
img172 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/AUS.png'
photos172 = ImageTk.PhotoImage(Image.open(img172))

#img173 = '/home/pi/python/intech_pic(CH)/Firstep-LOGO-gray.png'
# photos173=ImageTk.PhotoImage(Image.open(img173))
l = 'DESIGN'

img174 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/CalWarning.png'
photos174 = ImageTk.PhotoImage(Image.open(img174))
img175 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/CalError.png'
photos175 = ImageTk.PhotoImage(Image.open(img175))

img176 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/qrerror.png'
photos176 = ImageTk.PhotoImage(Image.open(img176))

img177 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/Success.png'
photos177 = ImageTk.PhotoImage(Image.open(img177))
img178 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/OKprinter.png'
photos178 = ImageTk.PhotoImage(Image.open(img178))

img179 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/BluePrinter_PleaseConnect.png'
photos179 = ImageTk.PhotoImage(Image.open(img179))

img180 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/btupdate.png'
photos180 = ImageTk.PhotoImage(Image.open(img180))

img181 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/BluetoothExport_PleaseConnect.png'
photos181 = ImageTk.PhotoImage(Image.open(img181))

img182 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/QueryBTPrinter.png'
photos182 = ImageTk.PhotoImage(Image.open(img182))

img183 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/settime_change.png'
photos183 = ImageTk.PhotoImage(Image.open(img183))

img184 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/keyboard_error.png'
photos184 = ImageTk.PhotoImage(Image.open(img184))

img185 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/Success_export.png'
photos185 = ImageTk.PhotoImage(Image.open(img185))

img186 = 'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/Bluetooth_Error.png'
photos186 = ImageTk.PhotoImage(Image.open(img186))


# new picture

QRcode = ImageTk.PhotoImage(Image.open(
    'C:/Users/USER/Desktop/convenience/GUI-photo(desktop)/qr_code.png'))


keyboard_show = 'matchbox-keyboard'

keyboard_show = 'matchbox-keyboard'


# item 這一整段都在寫說，選擇你的產品品項，子傑的機台預設是AMP(txt文字檔裡面存的是DP)
def itemshow(item):
    if item == "DA":
        return "MET"
    elif item == "DB":
        return "MOR"
    elif item == "DC":
        return "KET"
    else:
        return "unknown"


# result type read


def resulttype_read():
    f_resulttype = open(
        "C:/Users/USER/Desktop/convenience/Firstep/resulttype.txt", "r")
    resulttype = f_resulttype.readline()
    f_resulttype.close()
    resulttype = int(resulttype)
    return resulttype


def testtype_read():
    f_testtype = open("C:/Users/USER/Desktop/convenience/Firstep/testtype.txt", "r")
    testtype = f_testtype.readline().replace('\n', '')
    testtype = testtype.split(' ')
    testtype = testtype[0]
    f_testtype.close()
    return testtype

# test number read


def test_number_read():
    date = date_read()
    if os.path.exists('C:/Users/USER/Desktop/convenience/Firstep/test_number_'+date+'.txt'):
        f_test_number = open(
            "C:/Users/USER/Desktop/convenience/Firstep/test_number_"+date+".txt", "r")
        test_number_old = f_test_number.readline()
        f_test_number.close()
        test_number_old = int(test_number_old)
        return test_number_old
    else:
        test_number_old = 0
        return test_number_old


def testdata_number_read():
    if os.path.exists('C:/Users/USER/Desktop/convenience/Firstep/testdata_number.txt'):
        f_test_number = open(
            "C:/Users/USER/Desktop/convenience/Firstep/testdata_number.txt", "r")
        test_number_old = f_test_number.readline()
        f_test_number.close()
        test_number_old = int(test_number_old)
        return test_number_old
    else:
        test_number_old = 0
        return test_number_old


def testdata_number_write():
    test_number_old = testdata_number_read()
    test_number = test_number_old+1
    f_test_number = open(
        "C:/Users/USER/Desktop/convenience/Firstep/testdata_number.txt", "w")
    f_test_number.write(test_number.__str__())
    f_test_number.close()


def Cexist_read(M_Cexist_read):
    f_Cexist = open("C:/Users/USER/Desktop/convenience/Firstep/" +
                    M_Cexist_read+"_Cexist.txt", "r")
    Cexist = f_Cexist.readline()
    f_Cexist.close()
    Cexist = int(Cexist)

    return Cexist

# T2_item read


def T2_item_read(T2_item1):
    f_M_T2_item = open(
        "C:/Users/USER/Desktop/convenience/Firstep/"+T2_item1+"_item.txt", "r")
    M_T2_item = f_M_T2_item.readline()
    M_T2_item = itemshow(M_T2_item)  # 品項選擇，在最前面
    f_M_T2_item.close()

    return M_T2_item


# T1_item read


def T1_item_read(T1_item1):
    f_M_T1_item = open(
        "C:/Users/USER/Desktop/convenience/Firstep/"+T1_item1+"_item.txt", "r")
    M_T1_item = f_M_T1_item.readline()
    print(T1_item1)
    M_T1_item = itemshow(M_T1_item)
    print(M_T1_item)
    f_M_T1_item.close()

    return M_T1_item


def c_line_read():
    T1 = open("C:/Users/USER/Desktop/convenience/Firstep/c_line.txt", "r")
    c_line = T1.readline()
    T1.close()
    c_line = float(c_line)
    return c_line


def result_t1_read():
    T1 = open("C:/Users/USER/Desktop/convenience/Firstep/test.txt", "r")
    result_T1 = T1.readline()
    T1.close()
    result_T1 = float(result_T1)

    return result_T1


def result_t2_read():
    T2 = open("C:/Users/USER/Desktop/convenience/Firstep/test2.txt", "r")
    result_T2 = T2.readline()
    T2.close()
    result_T2 = float(result_T2)

    return result_T2


def setup():   
    GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
    GPIO.setup(6, GPIO.OUT)  # Set LedPin’s mode is output


def setup2():
    GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
    GPIO.setup(5, GPIO.OUT)  # Set LedPin’s mode is output


def openT(pin): 
    GPIO.output(pin, GPIO.HIGH)
    # time.sleep(100)
    return


def closeT(pin):
    GPIO.output(pin, GPIO.LOW)
    # time.sleep(100)
    return


def testing_c():
    COM_PORT = '/dev/ttyUSB0'
    BAUD_RATES = 9600
    ser = serial.Serial(COM_PORT, BAUD_RATES,timeout=10) 
    try:
        while True:
            while ser.in_waiting:          # 若收到序列資料… 
                print("開始計時")
                data_raw = ser.readline()
                print('接收到的校正訊息:',data_raw)               
                time.sleep(30)  
                a = 0
                while a<=20:             
                     data_raw = ser.readline()  #讀取一行
                     data = data_raw.decode()   # 用預設的UTF-8解碼
                     #print(a)
                     #print('接收到的校正電阻數值:',data)
                     if a == 15:
                         print('取頻率為1500之電阻值：', data)
                         path = '/home/pi/Firstep/c_line.txt'
                         f = open(path, 'w')
                         f.write(data+"歐姆".__str__())
                         f.close()
                     a+=1            
                setup()
                openT(6)                
                print('校正完成')
                print("開啟繼電器1")
                time.sleep(15)                
                b = 0
                while b<=20:
                    data_raw = ser.readline()  #讀取一行
                    data = data_raw.decode()   # 用預設的UTF-8解碼
                    #print(b)
                    #print('接收到的量測電阻值:',data)
                    if b == 15:
                        print('頻率為1500之量測電阻值1：', data)
                        path = '/home/pi/Firstep/testing1.txt'
                        f = open(path, 'w')
                        f.write(data+"歐姆".__str__())
                        f.close()
                    b+=1                          
                print('第一次量測完成')
                time.sleep(5)
                setup2()
                openT(5)
                print("開啟繼電器2")
                time.sleep(15) 
                c = 0
                while c<=20:
                    data_raw = ser.readline()  #讀取一行
                    data = data_raw.decode()   # 用預設的UTF-8解碼
                    #print(c)
                    #print('接收到的量測電阻值:',data)
                    if c == 15:
                        print('頻率為1500之量測電阻值2：', data)
                        path = '/home/pi/Firstep/testing2.txt'
                        f = open(path, 'w')
                        f.write(data+"歐姆".__str__())
                        f.close()
                    c+=1                          
                time.sleep(5)
                print('第二次量測完成')
                closeT(5)
                closeT(6)
            

                raise KeyboardInterrupt

    except KeyboardInterrupt:
        ser.close()
    finally:
        GPIO.cleanup()


def readID():
    p_ID = open("C:/Users/USER/Desktop/convenience/Firstep/PatientID.txt", "r")
    pid = p_ID.readline()
    p_ID.close()
    return pid
##################################################################################


def read_time():
    global year1
    global month1
    global date1
    global hour1
    global minute1

    year1 = datetime.now().strftime('%Y')
    month1 = datetime.now().strftime('%m')
    date1 = datetime.now().strftime('%d')
    hour1 = datetime.now().strftime('%H')
    minute1 = datetime.now().strftime('%M')

    return year1, month1, date1, hour1, minute1


def read_time1():
    global year11
    global month11
    global date11
    global hour11
    global minute11

    year11 = datetime.now().strftime('%Y')
    month11 = datetime.now().strftime('%m')
    date11 = datetime.now().strftime('%d')
    hour11 = datetime.now().strftime('%H')
    minute11 = datetime.now().strftime('%M')

    if (year != 0):
        year11 = str(year)
    if (month != 0):
        month11 = str(month)
    if (date != 0):
        date11 = str(date)
    if (hour != 0):
        hour11 = str(hour)
    if (minute != 0):
        minute11 = str(minute)

    if(len(month11) == 1):
        month11 = '0'+month11
    if(len(date11) == 1):
        date11 = '0'+date11
    if(len(year11) == 1):
        year11 = '0'+year11
    if(len(hour11) == 1):
        hour11 = '0'+hour11
    if(len(minute11) == 1):
        minute11 = '0'+minute11

    return year11, month11, date11, hour11, minute11


class SampleApp(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.switch_frame(StartPage)

    def switch_frame(self, c):
        '''Show a frame for the given class'''
        frame = c(root, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, height="600", width="800")

        def QRscanpage():
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            controller.switch_frame(QRscan)

        def setpage():
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            controller.switch_frame(Setting)

        def filepage():
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            controller.switch_frame(File)

        label1 = tk.Label(self, image=photo001)
        label1.place(x=0, y=60)

        btn1 = tk.Button(self, text="test", compound=BOTTOM, font=('Helvetica',32),
                         image=photo003, highlightthickness=0, bd=0, command=QRscanpage)
        btn2 = tk.Button(self, text="file", compound=BOTTOM, font=('Helvetica',32),
                         image=photo002, highlightthickness=0, bd=0, command=filepage)
        btn3 = tk.Button(self, text="setting", compound=BOTTOM, font=('Helvetica',32),
                         image=photo004, highlightthickness=0, bd=0, command=setpage)

        btn1.place(x=20, y=350)
        btn2.place(x=320, y=350)
        btn3.place(x=620, y=350)
        # 時間配置
        year1, month1, date1, hour1, minute1 = read_time()
        self.label12 = tk.Label(self, text=year1, font=1)
        self.label12.place(x=10, y=5)
        self.label13 = tk.Label(self, text=month1, font=1)
        self.label13.place(x=60, y=5)
        self.label14 = tk.Label(self, text=date1, font=1)
        self.label14.place(x=88, y=5)
        self.label15 = tk.Label(self, text=hour1, font=1)
        self.label15.place(x=138, y=5)
        self.label16 = tk.Label(self, text=minute1, font=1)
        self.label16.place(x=165, y=5)
        self.update()

    def update(self):
        year1, month1, date1, hour1, minute1 = read_time()
        self.label12.config(text=year1 + '-')
        self.label13.config(text=month1 + '-')
        self.label14.config(text=date1)
        self.label15.config(text=hour1 + ':')
        self.label16.config(text=minute1)
        self.after(1000, self.update)


class QRscan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, height="600", width="800")

        def btn22(*args):
            btn1.config(state='disabled')
            btn2.config(image=photo042)

        def btn222(*args):
            btn2.config(state='disabled')
            btn2.config(image=photo006)
            controller.switch_frame(StartPage)

        def itemchoose():
            n = str(entry1.get())
            if n == 'MET':
                T1_item1 = 'DA'
                T2_item2 = 'DA'
                # 改寫testtype文件
                f = open("C:/Users/USER/Desktop/convenience/testtype.txt", "w")
                f.write("1\n")
                f.close()
                controller.switch_frame(Test)
                return T1_item1, T2_item2
            elif n == 'MOR':
                T1_item1 = 'DB'
                T2_item2 = 'DB'
                f = open(
                    "C:/Users/USER/Desktop/convenience/Firstep/testtype.txt", "w")
                f.write("2\n")
                f.close()
                controller.switch_frame(Test)
                return T1_item1, T2_item2
            elif n == 'KET':
                T1_item1 = 'DC'
                T2_item2 = 'DC'
                f = open(
                    "C:/Users/USER/Desktop/convenience/Firstep/testtype.txt", "w")
                f.write("3\n")
                f.close()
                controller.switch_frame(Test)
                return T1_item1, T2_item2
            else:
                print("unknown")

        label1 = tk.Label(self,text='{:<22}'.format(t1)
                          , compound='top', font=('Helvetica', 40, "bold"))
        label1.place(x=8, y=120)
        entry1 = tk.Entry(self, font=('Helvetica', 60))
        entry1.place(x=50, y=280, width=450, height=120)
        btn1 = tk.Button(self, image=photo069,
                         highlightthickness=0, bd=0, command=itemchoose)
        btn2 = tk.Button(self, image=photo006, highlightthickness=0, bd=0)
        btn1.place(x=550, y=220)
        btn2.place(x=550, y=420)

        btn2.bind('<Button-1>', btn22)
        btn2.bind("<ButtonRelease-1>", btn222)

        year1, month1, date1, hour1, minute1 = read_time()
        self.label12 = tk.Label(self, text=year1, font=1)
        self.label12.place(x=10, y=5)
        self.label13 = tk.Label(self, text=month1, font=1)
        self.label13.place(x=60, y=5)
        self.label14 = tk.Label(self, text=date1, font=1)
        self.label14.place(x=88, y=5)
        self.label15 = tk.Label(self, text=hour1, font=1)
        self.label15.place(x=138, y=5)
        self.label16 = tk.Label(self, text=minute1, font=1)
        self.label16.place(x=165, y=5)
        self.update()

    def update(self):
        year1, month1, date1, hour1, minute1 = read_time()
        self.label12.config(text=year1 + '-')
        self.label13.config(text=month1 + '-')
        self.label14.config(text=date1)
        self.label15.config(text=hour1 + ':')
        self.label16.config(text=minute1)
        self.after(1000, self.update)


class Test(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, height="600", width="800")

        time.sleep(0.1)
        print("LED OFF!")

        pid = readID()

        def loading1():
            i = 0
            for i in range(4):
                global load
                self.label4 = tk.Label(self, image=photos_test1)
                self.label4.place(x=100, y=150)
                root.update_idletasks()
                time.sleep(2)
                self.label4 = tk.Label(self, image=photos_test2)
                self.label4.place(x=100, y=150)
                root.update_idletasks()
                time.sleep(2)
                self.label4 = tk.Label(self, image=photos_test3)
                self.label4.place(x=100, y=150)
                root.update_idletasks()
                time.sleep(2)
                print(i)

        def run_c():
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn5.config(state='disabled')
            runtest = threading.Thread(name='Test_c', target=testing_c)
            runtest.start()
            loading1()
            if runtest.is_alive():
                print('runtest Still running.')
            else:
                print('runtest Completed.')
            print('--------------------------------------------test line.--------------------------------------------')
            self.destroy()
            root.after(1000)
            controller.switch_frame(ButtonOK)
          
        def startpage():
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            # btn3.config(state='disabled')
            # btn4.config(state='disabled')
            btn5.config(state='disabled')
            controller.switch_frame(StartPage)

        def btn55(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn5.config(state='disabled')
            btn5.config(image=photo042)

        def btn555(*args):
            btn5.config(image=photo006)
            controller.switch_frame(QRscan)

        def btn44(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn5.config(state='disabled')
            btn2.config(image=photo005)

        def btn444(*args):
            btn2.config(image=photo041)
            startpage()

        def btn22(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn5.config(state='disabled')
            btn2.config(image=photo049)

        def btn222(*args):
            btn1.config(state='disabled')
            btn2.config(image=photo013)
            btn4.config(state='disabled')
            btn5.config(state='disabled')
            run_c()

        def btn11(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn5.config(state='disabled')
            btn1.config(image=photo066)

        def btn111(*args):
            btn1.config(image=photo035)
            global inputtxt
            inputtxt = 1
            controller.switch_frame(keyboard)

        def destroy(self):
            self.page.destroy()

        label1 = tk.Label(self, text=pid, font="Courier 40")
        label1.place(x=180, y=190)  # 受測者id位置
        btn1 = tk.Button(self, image=photo035, highlightthickness=0, bd=0)
        btn2 = tk.Button(self, image=photo013, highlightthickness=0, bd=0)
        btn4 = tk.Button(self, image=photo005, highlightthickness=0, bd=0)
        btn5 = tk.Button(self, image=photo006, highlightthickness=0, bd=0)
        btn1.place(x=100, y=70)
        btn2.place(x=550, y=100)  # test
        btn4.place(x=550, y=250)
        btn5.place(x=550, y=400)  # back

        btn1.bind('<Button-1>', btn11)
        btn1.bind("<ButtonRelease-1>", btn111)
        btn2.bind('<Button-1>', btn22)
        btn2.bind("<ButtonRelease-1>", btn222)
        btn4.bind('<Button-1>', btn44)
        btn4.bind("<ButtonRelease-1>", btn444)
        btn5.bind('<Button-1>', btn55)
        btn5.bind("<ButtonRelease-1>", btn555)

        testtype = str(testtype_read())
        resulttype = resulttype_read()

        # 檢測結果顯示
        # def pos_show_1C1T(result_text, x, label_resulttype_pos, label_item_pos, item):
        #     label_resulttype = tk.Label(
        #         self, text=result_text, font="Courier 14")
        #     # y參數可以改成200，label_resulttype_pos
        #     label_resulttype.place(x=x, y=label_resulttype_pos)
        #     label_item = tk.Label(self, text='品項:' + item, font="Courier 14")
        #     # 150    ##y參數可以改成250，label_resulttype_pos
        #     label_item.place(x=x, y=label_item_pos)
        #     print(label_item_pos)
        #     print("是這行沒錯")

        def pos_show_1C2T(result_text, x, label_resulttype_pos, label_c_line_pos, label_item_pos, label_item1_pos, item, item1):
            label_resulttype = tk.Label(
                self, text=result_text, font="Courier 28")
            label_resulttype.place(x=x, y=label_resulttype_pos)  # 150
            label_c_line = tk.Label(self, text="C線判斷:", font="Courier 28")
            label_c_line.place(x=x, y=label_c_line_pos)
            label_item = tk.Label(self, text='T1品項:'+item, font="Courier 28")
            label_item.place(x=x, y=label_item_pos)  # 200
            label_item1 = tk.Label(self, text='T2品項:'+item1, font="Courier 28")
            label_item1.place(x=x, y=label_item1_pos)  # 250
            

        def resulttype_check():
            if resulttype == 1:
                result_text_A = "定性"

            elif resulttype == 2:
                result_text_A = "定量"

            return result_text_A

        # M_choose

        # 只留1C2T
        if testtype == "1":
            A_item = T1_item_read("A")
            A_item_t2 = T2_item_read("A")
            print("A_item =", A_item)

            result_text_A = resulttype_check()
            # pos_show_1C2T(result_text, x, label_resulttype_pos, label_c_line_pos, label_item_pos, label_item1_pos, item, item1):
            pos_show_1C2T(result_text_A, 15, 270, 330,
                          390, 450, A_item, A_item_t2)
            # ('c', A_c_concentration, 250, A_item_T2, A_item_T1, A_t2_concentration,
            # , A_t2_result_c, A_t1_result_c, 10, 30, 300, 350)
        elif testtype == "2":
            A_item = T1_item_read("B")
            A_item_t2 = T2_item_read("B")
            print("A_item =", A_item)

            result_text_A = resulttype_check()

            pos_show_1C2T(result_text_A, 15, 270, 330,
                          390, 450, A_item, A_item_t2)
            # ('c', A_c_concentration, 250, A_item_T2, A_item_T1, A_t2_concentration,
            # A_t1_concentration, A_t2_result_c, A_t1_result_c, 10, 30, 300, 350)
        elif testtype == "3":
            A_item = T1_item_read("C")
            A_item_t2 = T2_item_read("C")
            print("A_item =", A_item)

            result_text_A = resulttype_check()

            pos_show_1C2T(result_text_A, 15, 270, 330,
                          390, 450, A_item, A_item_t2)
            # ('c', A_c_concentration, 250, A_item_T2, A_item_T1, A_t2_concentration,
            # , A_t2_result_c, A_t1_result_c, 10, 30, 300, 350)
        else:
            print("Error,what the hell do you mean")

        year1, month1, date1, hour1, minute1 = read_time()
        self.label12 = tk.Label(self, text=year1, font=1)
        self.label12.place(x=10, y=5)
        self.label13 = tk.Label(self, text=month1, font=1)
        self.label13.place(x=60, y=5)
        self.label14 = tk.Label(self, text=date1, font=1)
        self.label14.place(x=88, y=5)
        self.label15 = tk.Label(self, text=hour1, font=1)
        self.label15.place(x=138, y=5)
        self.label16 = tk.Label(self, text=minute1, font=1)
        self.label16.place(x=165, y=5)
        self.update()

    def update(self):
        year1, month1, date1, hour1, minute1 = read_time()
        self.label12.config(text=year1 + '-')
        self.label13.config(text=month1 + '-')
        self.label14.config(text=date1)
        self.label15.config(text=hour1 + ':')
        self.label16.config(text=minute1)
        self.after(1000, self.update)


class ButtonOK(tk.Frame):
    def __init__(self, parent, controller, master=None):
        self.page = tk.Frame.__init__(self, parent, master)
        btn1 = tk.Button(self, text=" ", highlightthickness=0, bd=0)
        btn1.grid(row=0, column=0, padx=212, pady=418)

        def date_read_old():
            f_date_read = open(
                "C:/Users/USER/Desktop/convenience/Firstep/date_count.txt", "r")
            date_old = f_date_read.readline()
            f_date_read.close()
            return date_old

        def data_quantity_read():
            f_data_quantity = open(
                "C:/Users/USER/Desktop/convenience/Firstep/data_quantity.txt", "r")
            data_quantity_old = f_data_quantity.readline()
            f_data_quantity.close()
            data_quantity_old = int(data_quantity_old)
            return data_quantity_old

        def data_quantity_write():
            data_quantity_old = data_quantity_read()
            data_quantity = data_quantity_old+1
            f_data_quantity = open(
                "C:/Users/USER/Desktop/convenience/data_quantity.txt", "w")
            f_data_quantity.write(data_quantity.__str__())
            f_data_quantity.close()

        def data_quantity_write1():
            data_quantity = 1
            f_data_quantity = open(
                "C:/Users/USER/Desktop/convenience/data_quantity.txt", "w")
            f_data_quantity.write(data_quantity.__str__())
            f_data_quantity.close()

        def testdata_number_read():
            if os.path.exists('C:/Users/USER/Desktop/convenience/testdata_number.txt'):
                f_test_number = open(
                    "/C:/Users/USER/Desktop/convenience/testdata_number.txt", "r")
                test_number_old = f_test_number.readline()
                f_test_number.close()
                test_number_old = int(test_number_old)
                return test_number_old
            else:
                test_number_old = 0
                return test_number_old

        def testdata_number_write():
            test_number_old = testdata_number_read()
            test_number = test_number_old+1
            testnumber = str(test_number)
            print('testnumber :', testnumber)

            f_test_number = open(
                "C:/Users/USER/Desktop/convenience/testdata_number.txt", "w")
            f_test_number.write(test_number.__str__())
            f_test_number.close()

            return testnumber

############################################################
        def c_line_check():
            c_line = float(c_line_read())
            return c_line

        # 判斷c線有無的程式(判斷試劑是否有效)

        def resultshow_1C1T(M):
            Cexist = Cexist_read(M)
            print("Cexist = ", Cexist)

            resulttype = resulttype_read()
            print("resulttype = ", resulttype)

            if Cexist == 1:
                print("cline exist")
                a = 500
                b = 750
                c = 1000
                result_t1 = float(result_t1_read())

                # t_concentration = t2_GS
                # t_concentration = "%4.1f" % t_concentration
                # t_concentration = float(t_concentration)
                # t_concentration = 255-t_concentration
                # t2_GS = (t_concentration-T2_B/T2_A)
                # print("t2_GS =", t2_GS)

                # if resulttype == 1 or resulttype == 3:
                #     if t2_GS >= T2cutoff:
                #         return '陽性'
                #     else:
                #         return '陰性'

                # elif resulttype == 2 or resulttype == 4:
                #     if t2_GS < T2cutoff:
                #         t2_GS = '<'+"%4.1f" % T2cutoff+' ng/mL'
                #         return t2_GS+' 陰性'
                #     elif T2cutoff <= t2_GS <= T2uppercutoff:
                #         t2_GS = "%4.1f" % t2_GS+' ng/mL'
                #         return t2_GS
                #         print(t2_GS)
                #     elif t2_GS > T2uppercutoff:
                #         t2_GS = '>='+"%4.1f" % T2uppercutoff+' ng/mL'
                #         return t2_GS+' 強陽性'

                if resulttype == 1:
                    if result_t1 >= b:
                        result_t1 = '陽性'
                    else:
                        result_t1 = '陰性'
                    # ---------------------------------

                elif resulttype == 2:
                    # result_t1
                    if result_t1 < a:
                        result = '<500'
                        return result+' 結果為陰性'
                    elif a <= result_t1 < b:
                        result = '500<result<750'
                        return result+' 結果為弱陽性'
                    elif b <= result_t1 < c:
                        result = '750<result<1000'
                        return result+' 結果為中陽性'
                    elif result_t1 >= c:
                        result = '>=1000'
                        return result+' ,結果為強陽性'

                # elif resulttype == 2:  # or resulttype == 4:     數字區間判斷
                #     if result_t1 < a:
                #         result = '<500'
                #         return result+' 結果為陰性'
                #     elif a <= result_t1 < b:
                #         result = "%4.1f" % result_t1
                #         return result
                #     elif b <= result_t1 < c:
                #         result = "%4.1f" % result_t1
                #         return result
                #     elif result_t1 >= c:
                #         result = '>=1000'
                #         return result+' ,結果為強陽性'

            else:  # invalid strip
                print("no Cline, invalid strip : light yello")
                return '無效'

############################################################
        def resultshow_1C2T(M):

            Cexist = Cexist_read(M)
            print("Cexist = ", Cexist)

            resulttype = resulttype_read()
            print("resulttype = ", resulttype)

            if Cexist == 1:  # Cline exist
                print("cline exist")
                a = 500
                b = 750
                c = 1000

                result_t2 = float(result_t2_read())
                # float(result_t1_read())
                # print("t1_GS =", t1_GS)

                # t1_result_c = math.fabs(float(t1_GS)/float(c_GS))
                # t2_result_c = math.fabs(float(t2_GS)/float(c_GS))
                # t1_result_c = "%4.3f" % t1_result_c
                # t2_result_c = "%4.3f" % t2_result_c

                # print('12341552346', t1_result_c, t2_result_c)

                # t2_concentration=t2_GS
                # t2_concentration="%4.1f" % t2_concentration # prevent carry issue
                # t2_concentration=float(t2_concentration)
                # t2_concentration=255-t2_concentration
                # t2_GS=(t2_concentration-T2_B)/T2_A
                # print "t2_GS =",t2_GS
                #                 #---------------------------------

                # t1_concentration=t1_GS
                # t1_concentration="%4.1f" % t1_concentration # prevent carry issue
                # t1_concentration=float(t1_concentration)
                # t1_concentration=255-t1_concentration
                # t1_GS=(t1_concentration-T1_B)/T1_A
                # print "t1_GS =",t1_GS

                if resulttype == 1:
                    if result_t2 >= b:
                        result_t2 = '陽性'
                    else:
                        result_t2 = '陰性'

                # elif resulttype == 2 or resulttype == 4:
                #     c_GS = "%4.3f" % c_GS  # 2021.01.15_改
                #     t2_GS = "%4.3f" % t2_GS
                #     t1_GS = "%4.3f" % t1_GS
                #       判斷式
                #     if t2_GS < T2cutoff:
                #         t2_GS='<'+"%4.1f" % T2cutoff+' ng/mL'+' 陰性'
                #     elif T2cutoff <= t2_GS <= T2uppercutoff:
                #          t2_GS="%4.1f" % t2_GS+' ng/mL'
                #     elif t2_GS > T2uppercutoff:
                #          t2_GS='>='+"%4.1f" % T2uppercutoff+' ng/mL'+' 強陽性'
                #                         #---------------------------------
                #     if t1_GS < T1cutoff:
                #         t1_GS='<'+"%4.1f" % T1cutoff+' ng/mL'+' 陰性'
                #     elif T1cutoff <= t1_GS <= T1uppercutoff:
                #         t1_GS="%4.1f" % t1_GS+' ng/mL'
                #     elif t1_GS > T1uppercutoff:
                #         t1_GS='>='+"%4.1f" % T1uppercutoff+' ng/mL'+' 強陽性'

                # return c_GS, t2_GS, t1_GS, t2_result_c, t1_result_c
                # return t2_GS,t1_GS,t1_t,t2_t,c

                elif resulttype == 2:

                    if result_t2 < a:
                        result = '<500'
                        return result+' 結果為陰性'
                    elif a <= result_t2 < b:
                        result = '500<result<750'
                        return result+' 結果為弱陽性'
                    elif b <= result_t2 < c:
                        result = '750<result<1000'
                        return result+' 結果為中陽性'
                    elif result_t2 >= c:
                        result = '>=1000'
                        return result+' ,結果為強陽性'
                    # c_GS = "%4.3f" % c_GS  # 2021.01.15_改
                    # result_t2 = "%4.3f" % result_t2
                    # result_t1 = "%4.3f" % result_t1

                    # if result_t2 < float(b):
                    #     result_t2 = '<'+"%4.1f" % result_t2+' 歐姆'+' 陰性'
                    # elif float(b) <= result_t2 <= float(c):
                    #     result_t2 = "%4.1f" % result_t2+' 歐姆'
                    # elif result_t2 > float(c):
                    #     result_t2 = '>='+"%4.1f" % float(a) + ' 歐姆'+' 強陽性'
                    # print(result_t2)
                    # # ---------------------------------
                    # if result_t1 < float(b):
                    #     result_t1 = '<500'+' 歐姆'+' 陰性'
                    # elif float(b) <= result_t1 <= float(c):
                    #     result_t1 = "%4.1f" % result_t1 + ' 歐姆'
                    # elif result_t1 > float(c):
                    #     result_t1 = '>= 900'+' 歐姆'+' 強陽性'
                    # print(result_t1)

                    # if result_t2 < float(b):
                    #     result_t2 = '<'+"%4.1f" % result_t2
                    # elif float(b) <= result_t2 <= float(c):
                    #     result_t2 = "%4.1f" % result_t2
                    # elif result_t2 > float(c):
                    #     result_t2 = '>='+"%4.1f" % float(a)
                    # print(result_t2)
                    # ---------------------------------
                    # if result_t1 < float(b):
                    #     result_t1 = '<500'
                    # elif float(b) <= result_t1 <= float(c):
                    #     result_t1 = "%4.1f" % result_t1
                    # elif result_t1 > float(c):
                    #     result_t1 = '>= 900'
                    # print(result_t1)

                # return result_t1, result_t2
            else:  # invalid strip
                print("no Cline, invalid strip : light yello")
                return '無效', '無效', '無效', '無效', '無效'

############################################################
       # button ok 部分的主程式開始
        date = date_read()
        print('date: ', date)

        todaytime = time_read()
        print('todaytime: ', todaytime)

        testtype = str(testtype_read())
        print('testtype: ', testtype)

        resulttype = resulttype_read()
        print('resulttype: ', resulttype)

        # os.system('sudo chmod 777 /home/pi/Firstep/data.db')

        date_now = date.split('-')  # --------------------更動時間開始
        print('date_now: ', date_now)
        print('date_now[2]= ', date_now[2])

        date_old = date_read_old()
        print('date_old= ', date_old)

        if date_old == date_now[2]:
            print('日期未更動')
            show_date = ''
            print('日期 :空格')
            data_quantity_write()

        else:
            print('日期更動')
            show_date = date_now[1]+'月'+date_now[2]+'日'
            print('日期(show_date) : ', show_date)
            data_quantity_write1()
            date_write = open(
                "C:/Users/USER/Desktop/convenience/Firstep/date_count.txt", "w")
            date_write.write(date_now[2].__str__())
            date_write.close()  # --------------------更動時間結束

        print('show_date: ', show_date)

        pid = readID()
        print("ID:", pid)

        conn = sqlite3.connect('C:/Users/USER/Desktop/convenience/TEST2.db')
        conn.text_factory = str
        print("Opened database successfully")

        testtime = date+'/'+todaytime
        print('testtime: ', testtime)

        datein = date.split('-')
        print('datein: ', datein)

        yearin = datein[0].split()
        print('yearin: ', yearin)
        yearin1 = str(yearin)

        data_quantity_old = data_quantity_read()
        f_data_quantity_old = str(data_quantity_old)
        if len(f_data_quantity_old) == 1:
            f_data_quantity_old = '00'+f_data_quantity_old

        elif len(f_data_quantity_old) == 2:
            f_data_quantity_old = '0'+f_data_quantity_old

        else:
            f_data_quantity_old = f_data_quantity_old

        file_name = str(machine_number)+'-' + \
            yearin1[2:6]+datein[1]+datein[2]+'-'+f_data_quantity_old
        print('file_name: ', file_name)

        def BTprint():
            try:
                subprocess.call("sudo /etc/init.d/cups restart".split())
                subprocess.call("sudo /etc/init.d/bluetooth start".split())

                f1 = codecs.open("C:/Users/USER/Desktop/convenience/Firstep/Print.txt",
                                 "r", encoding='utf-8')
                print("cross line")
                f2 = codecs.open(
                    "C:/Users/USER/Desktop/convenience/bluePrinter.txt", "r", encoding='utf-8')
                text = f1.readlines()
                addr = f2.readline()
                f2.close()
                print("檢測完的馬上列印")
                print(text)
                print("In Print state ------------------------Do Prin")
                print("讀取文檔後Address:"), addr
                bd_addr = addr
                port = 1
                sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                sock.connect((bd_addr, port))
                print("內容顯示:")
                for result in text:
                    # result = repr(result)  # repr(object)轉換成為閱讀器閱讀的形式
                    # result = result.strip("'\ufeff'")
                    # print(result)
                    # result = unicode(result, 'big5')  這個是python2的寫法
                    # result = str(result, 'big5')

                    # result = result.decode('unicode-escape')

                    sock.send(result.encode('big5'))
                    # sock.send(result.encode('GB18030'))
                sock.send('\n\n\n')
                sock.close()
                print("Print successful")
                self.label5 = tk.Label(self, image=photos177)
                self.label5.place(x=16, y=58)

                self.printOK = tk.Button(
                    self, image=photo026, command=printprocess_finish)
                self.printOK.place(x=125, y=140)
            except:
                print("Print fail")
                print("讀取文檔後Address:"), addr
                self.label5 = tk.Label(self, image=photos178)
                self.label5.place(x=100, y=150)

                self.printOK = tk.Button(
                    self, image=photo026, command=printprocess_finish)
                self.printOK.place(x=315, y=300)

        def printprocess_finish():
            btn_print.config(state='normal')
            btn_home.config(state='normal')
            btn_back.config(state='normal')
            self.printOK.place_forget()
            self.label4.place_forget()
            self.label5.place_forget()

        def loading():
            print("loading")
            self.label4 = tk.Label(self, image=photos36)
            self.label4.place(x=100, y=150)

        def printing():
            print("print-------------------------------------------------------------------------------------------------------------------------------------")
            printing = threading.Thread(name='Print', target=BTprint)
            printing.start()
            loading()
            if printing.is_alive():
                print('runtest Still running.')
            else:
                print('runtest Completed.')

        def btn_print_down(*args):
            btn_home.config(state='disabled')
            btn_back.config(state='disabled')
            btn_print.config(image=photo056)

        def btn_print_up(*args):
            btn_print.config(image=photo015)
            btn_print.config(state='disabled')
            printing()

        def btn_home_down(*args):
            btn_print.config(state='disabled')
            # btn2.config(state='disabled')
            btn_back.config(state='disabled')
            btn_home.config(image=photo041)

        def btn_home_up(*args):
            btn_home.config(image=photo005)
            time.sleep(1)
            controller.switch_frame(StartPage)

        def btn_back_down(*args):
            btn_print.config(state='disabled')
            btn_home.config(state='disabled')
            # btn3.config(state='disabled')
            btn_back.config(image=photo042)

        def btn_back_up(*args):
            btn_back.config(image=photo006)
            # self.destroy()
            controller.switch_frame(Test)

        def destroy(self):
            self.page.destroy()


#####################################################

        # def pos_show_1C2T(c, c_result, c_y_pos, item_T2, item_T1, t2_result, t1_result, t2_result_c, t1_result_c, label_1C2T_item_x_pos, label_1C2T_result_x_pos, t2_y_pos, t1_y_pos):

        #     label = tk.Label(self, text="受測者編碼 :"+pid,
        #                      padx=0, font='Courier 14')
        #     label.place(x=10, y=120)  # EN

        #     label_c_item = tk.Label(
        #         self, text=c+' / '+c_result, font='Courier 14')
        #     label_c_item.place(x=label_1C2T_item_x_pos, y=c_y_pos)  # 130

        #     label_1C2T_t2_item = tk.Label(
        #         self, text=item_T2+' / '+t2_result, font='Courier 14')
        #     label_1C2T_t2_item.place(
        #         x=label_1C2T_item_x_pos, y=t2_y_pos)  # 130
        #     label_1C2T_t1_item = tk.Label(
        #         self, text=item_T1+' / '+t1_result, font='Courier 14')
        #     label_1C2T_t1_item.place(
        #         x=label_1C2T_item_x_pos, y=t1_y_pos)  # 170

        #     label_1C2T_t2_text = tk.Label(
        #         self, text=t2_result_c, font='Courier 14')
        #     label_1C2T_t2_text.place(
        #         x=label_1C2T_result_x_pos, y=t2_y_pos+20)  # 150

        #     label_1C2T_t1_text = tk.Label(
        #         self, text=t1_result_c, font='Courier 14')
        #     label_1C2T_t1_text.place(
        #         x=label_1C2T_result_x_pos, y=t1_y_pos+20)  # 190

        if testtype == "1":
            c_line = c_line_check()
            c_line = str(c_line)
            A_t1_concentration = resultshow_1C1T("A")
            A_t2_concentration = resultshow_1C2T("A")
            print("A_t1_concentration =", A_t1_concentration)

            A_item_T1 = T1_item_read("A")
            A_item_T2 = T2_item_read("A")
            print("A_item =", A_item_T1)
            Impedance_1 = float(result_t1_read())
            Impedance_2 = float(result_t2_read())
            # pos_show_1C1T(A_item, A_t2_concentration, 10, 130, 150, 170)

            test_number = testdata_number_write()
            print(test_number, resulttype, testtype, pid, testtime, show_date,
                  file_name, A_item_T1, A_t2_concentration, Impedance_1)

            conn.execute("INSERT INTO TEST2 (ID,Resulttype,Testtype,PatientID,TIME,SHOW_DATE,FILE_NAME,item,c_line,T1,T2,Impedance_T1,Impedance_T2) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                test_number, resulttype, testtype, pid, testtime, show_date, file_name, A_item_T1, c_line, A_t1_concentration, A_t2_concentration, Impedance_1, Impedance_2))
            print("Records created successfully")

            # 待修
            Print = (' 機碼 :'+str(machine_number).strip()+'\n'+' 測試時間 :'+testtime.strip()+'\n'+' 受測者編碼 :'+pid.strip()+'\n'+' 品項 :'+A_item_T1.strip(
            )+'\n'+' T1檢測值 :'+'\n'+' '+A_t1_concentration.strip()+'\n'+' T2檢測值 :'+'\n'+' '+A_t2_concentration.strip()+'\n''--------------------------------'+'\n'+' 列印時間 :'+todaytime)

        elif testtype == "2":
            c_line = c_line_check()
            c_line = str(c_line)
            A_t1_concentration = resultshow_1C1T("B")
            A_t2_concentration = resultshow_1C2T("B")
            print("A_t1_concentration =", A_t1_concentration)

            print("testtype = 2,Flu B")
            A_item_T1 = T1_item_read("B")
            A_item_T2 = T2_item_read("B")
            print("A_item =", A_item_T1)
            Impedance_1 = float(result_t1_read())
            Impedance_2 = float(result_t2_read())

            # A_c_concentration, A_t2_concentration, A_t1_concentration, A_t2_result_c, A_t1_result_c = resultshow_1C2T(
            #     "B")
            # print("result ="), A_t2_concentration, A_t1_concentration

            # pos_show_1C2T('c', A_c_concentration, 250, A_item_T2, A_item_T1, A_t2_concentration,
            #               A_t1_concentration, A_t2_result_c, A_t1_result_c, 10, 30, 300, 350)

            test_number = testdata_number_write()

            conn.execute("INSERT INTO TEST2 (ID,Resulttype,Testtype,PatientID,TIME,SHOW_DATE,FILE_NAME,item,c_line,T1,T2,Impedance_T1,Impedance_T2) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                test_number, resulttype, testtype, pid, testtime, show_date, file_name, A_item_T1, c_line, A_t1_concentration, A_t2_concentration, Impedance_1, Impedance_2))
            print("Records created successfully")

            # 待修
            Print = (' 機碼 :'+str(machine_number).strip()+'\n'+' 測試時間 :'+testtime.strip()+'\n'+' 受測者編碼 :'+pid.strip()+'\n'+' 品項 :'+A_item_T1.strip(
            )+'\n'+' T1檢測值 :'+'\n'+' '+A_t1_concentration.strip()+'\n'+' T2檢測值 :'+'\n'+' '+A_t2_concentration.strip()+'\n''--------------------------------'+'\n'+' 列印時間 :'+todaytime)

        elif testtype == "3":
            c_line = c_line_check()
            c_line = str(c_line)
            A_t1_concentration = resultshow_1C1T("C")
            A_t2_concentration = resultshow_1C2T("C")
            print("A_t1_concentration =", A_t1_concentration)

            A_item_T1 = T1_item_read("C")
            A_item_T2 = T2_item_read("C")
            print("A_item =", A_item_T1)
            Impedance_1 = float(result_t1_read())
            Impedance_2 = float(result_t2_read())

            test_number = testdata_number_write()

            conn.execute("INSERT INTO TEST2 (ID,Resulttype,Testtype,PatientID,TIME,SHOW_DATE,FILE_NAME,item,c_line,T1,T2,Impedance_T1,Impedance_T2) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                test_number, resulttype, testtype, pid, testtime, show_date, file_name, A_item_T1, c_line, A_t1_concentration, A_t2_concentration, Impedance_1, Impedance_2))
            print("Records created successfully")
            # 待修
            Print = (' 機碼 :'+str(machine_number).strip()+'\n'+' 測試時間 :'+testtime.strip()+'\n'+' 受測者編碼 :'+pid.strip()+'\n'+' 品項 :'+A_item_T1.strip(
            )+'\n'+' T1檢測值 :'+'\n'+' '+A_t1_concentration.strip()+'\n'+' T2檢測值 :'+'\n'+' '+A_t2_concentration.strip()+'\n''--------------------------------'+'\n'+' 列印時間 :'+todaytime)
        else:
            print("Error")

        conn.commit()
        conn.close()

        f_Print = open(
            "C:/Users/USER/Desktop/convenience/Firstep/Print.txt", "w")
        f_Print.write(Print)
        f_Print.close()
        print("------------------------------------------")
        # print(Print)
        print("------------------------------------------")

        label_number = tk.Label(self, text="受測者編碼 :"+pid,
                                padx=0, font='Courier 14')
        label_number.place(x=10, y=110)

        label_item = tk.Label(self, text='品項:' + A_item_T1,
                              padx=0, font='Courier 22')  # item
        label_item.place(x=10, y=160)  # EN

        label_c_line = tk.Label(self, text='C線數值:' + c_line,
                                padx=0, font='Courier 22')  # item)
        label_c_line.place(x=10, y=210)

        label_T1 = tk.Label(self, text='T1檢測結果:'+'\n' + str(result_t1_read())+'歐姆',
                            padx=0, font='Courier 22')
        label_T1.place(x=10, y=260)  # T1

        label_T2 = tk.Label(self, text='T2檢測結果:'+'\n' + str(result_t2_read())+'歐姆',
                            padx=0, font='Courier 22')
        label_T2.place(x=10, y=310)  # T2

        btn_print = tk.Button(self, image=photo015, highlightthickness=0, bd=0)
        btn_home = tk.Button(self, image=photo005, highlightthickness=0, bd=0)
        btn_back = tk.Button(self, image=photo006, highlightthickness=0, bd=0)
        btn_print.place(x=550, y=20)
        btn_home.place(x=550, y=220)
        btn_back.place(x=550, y=420)

        btn_print = tk.Button(self, image=photo015, highlightthickness=0, bd=0)
        btn_home = tk.Button(self, image=photo005, highlightthickness=0, bd=0)
        btn_back = tk.Button(self, image=photo006, highlightthickness=0, bd=0)
        btn_print.place(x=230, y=100)
        btn_home.place(x=230, y=200)
        btn_back.place(x=230, y=250)

        btn_print.bind('<Button-1>', btn_print_down)
        btn_print.bind("<ButtonRelease-1>", btn_print_up)
        btn_home.bind('<Button-1>', btn_home_down)
        btn_home.bind("<ButtonRelease-1>", btn_home_up)
        btn_back.bind('<Button-1>', btn_back_down)
        btn_back.bind("<ButtonRelease-1>", btn_back_up)

        year1, month1, date1, hour1, minute1 = read_time()
        self.label12 = tk.Label(self, text=year1, font=1)
        self.label12.place(x=10, y=5)
        self.label13 = tk.Label(self, text=month1, font=1)
        self.label13.place(x=60, y=5)
        self.label14 = tk.Label(self, text=date1, font=1)
        self.label14.place(x=88, y=5)
        self.label15 = tk.Label(self, text=hour1, font=1)
        self.label15.place(x=138, y=5)
        self.label16 = tk.Label(self, text=minute1, font=1)
        self.label16.place(x=165, y=5)
        self.update()

    def update(self):
        year1, month1, date1, hour1, minute1 = read_time()
        self.label12.config(text=year1 + '-')
        self.label13.config(text=month1 + '-')
        self.label14.config(text=date1)
        self.label15.config(text=hour1 + ':')
        self.label16.config(text=minute1)
        self.after(1000, self.update)


class BluetoothExport(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # BluetoothExport and ClearData page.

        def bluetoothexport():
            global channel
            f = open("C:/Users/USER/Desktop/convenience/blueStorage.txt", "r")
            s = f.readline()
            print("讀取文檔後Address:", s)
            f.close()
            os.system("sudo sh /home/pi/blue.sh")
            print('111111111111')

            print(channel)  # it is the correct channel, I've doubled checked
            if channel == -1:
                print('失敗')
                self.label5 = tk.Label(self, image=photos179)
                self.label5.place(x=2, y=85)
                self.btnExport = tk.Button(
                    self, image=photo026, highlightthickness=0, bd=0, command=exportok)
                self.btnExport.place(x=82, y=142)

            else:
                print("---------Make Excel---------")
                print("part 1")
                todaytime = datetime.now().strftime('%H-%M-%S')
                timein = date_read()+'_'+todaytime
                conn = sqlite3.connect(
                    'C:/Users/USER/Desktop/convenience/TEST2.db')
                cursor = conn.execute("SELECT * from TEST2")
                f_exportxls = 'C:/Users/USER/Desktop/convenience/'+machine_number+'_'+timein+'.xls'
                w = xlwt.Workbook()
                w = xlwt.Workbook(encoding='utf-8')  # 使excel輸出中文
                t = w.add_sheet('data', cell_overwrite_ok=True)  # 添加一個sheet
                t.write(0, 0, 'No.')  # 開始寫入數據
                t.write(0, 1, "受測者編碼")
                t.write(0, 2, 'Item')
                t.write(0, 3, 'c線判斷')
                t.write(0, 5, '陰陽性判斷_T1')
                t.write(0, 7, '陰陽性判斷_T2')
                t.write(0, 9, '實際數據值_T1')
                t.write(0, 11, '實際數據值_T2')
                t.write(0, 13, 'Time')
                insertnum = 0
                for row in cursor:
                    insertnum = insertnum+1
                    print('Test Type row[2]: ', row[2])
                    if row[2] == 1:
                        print('Result Type row[1]: ', row[1])
                        t.write(insertnum, 0, str(row[0]))  # No.
                        t.write(insertnum, 1, row[3])  # id
                        t.write(insertnum, 2, row[7])  # A_item
                        t.write(insertnum, 3, row[8])  # A_item
                        t.write(insertnum, 5, row[9])  # A_RESULT_T1
                        t.write(insertnum, 7, row[10])  # A_RESULT_T2
                        t.write(insertnum, 9, row[11])  # Impedance_T1
                        t.write(insertnum, 11, row[12])  # Impedance_T2
                        t.write(insertnum, 13, row[4])   # time
                        print(
                            '------------------------------------------------------')
                    elif row[2] == 2:
                        print('Result Type row[1]: ', row[1])
                        t.write(insertnum, 0, str(row[0]))  # No.
                        t.write(insertnum, 1, row[3])  # id
                        t.write(insertnum, 2, row[7])  # A_item
                        t.write(insertnum, 3, row[8])  # A_item
                        t.write(insertnum, 5, row[9])  # A_RESULT_T1
                        t.write(insertnum, 7, row[10])  # A_RESULT_T2
                        t.write(insertnum, 9, row[11])  # Impedance_T1
                        t.write(insertnum, 11, row[12])  # Impedance_T2
                        t.write(insertnum, 13, row[4])   # time

                        t.write(insertnum+1, 0, str(row[0]))  # No.
                        t.write(insertnum+1, 1, row[3])  # id
                        t.write(insertnum+1, 2, row[7])  # A_item
                        t.write(insertnum+1, 3, row[8])  # A_RESULT_T1
                        t.write(insertnum+1, 5, row[9])  # A_RESULT_T1
                        t.write(insertnum+1, 7, row[10])  # A_RESULT_T2
                        t.write(insertnum+1, 9, row[11])  # Impedance_T1
                        t.write(insertnum+1, 11, row[12])  # Impedance_T2
                        t.write(insertnum+1, 13, row[4])   # time
                        insertnum = insertnum+1
                        print(
                            '------------------------------------------------------')
                    elif row[2] == 3:
                        print('Result Type row[1]: ', row[1])
                        t.write(insertnum, 0, str(row[0]))  # No.
                        t.write(insertnum, 1, row[3])  # id
                        t.write(insertnum, 2, row[7])  # A_item
                        t.write(insertnum, 3, row[8])  # A_item
                        t.write(insertnum, 5, row[9])  # A_RESULT_T1
                        t.write(insertnum, 7, row[10])  # A_RESULT_T2
                        t.write(insertnum, 9, row[11])  # Impedance_T1
                        t.write(insertnum, 11, row[12])  # Impedance_T2
                        t.write(insertnum, 13, row[4])   # time

                        t.write(insertnum+1, 0, str(row[0]))  # No.
                        t.write(insertnum+1, 1, row[3])  # id
                        t.write(insertnum+1, 2, row[7])  # A_item
                        t.write(insertnum+1, 3, row[8])  # A_RESULT_T1
                        t.write(insertnum+1, 5, row[9])  # A_RESULT_T1
                        t.write(insertnum+1, 7, row[10])  # A_RESULT_T2
                        t.write(insertnum+1, 9, row[11])  # Impedance_T1
                        t.write(insertnum+1, 11, row[12])  # Impedance_T2
                        t.write(insertnum+1, 13, row[4])   # time
                        insertnum = insertnum+1
                        print(
                            '------------------------------------------------------')

                print("---------for loop done---------")
                w.save(f_exportxls)
                time.sleep(3)

                print("---------Sending---------")
                os.system('sdptool search --bdaddr '+s+' OPUSH')
                os.system('obexftp --nopath --noconn --uuid none --bluetooth ' +
                          s+' --channel 12 --put ' + 'C:/Users/USER/Desktop/convenience/'+machine_number+'_'+timein+'.xls')

                time.sleep(5)
                print('成功')
                self.label5 = tk.Label(self, image=photos185)
                self.label5.place(x=2, y=85)

                self.btnExport = tk.Button(
                    self, image=photo026, command=exportok)
                self.btnExport.place(x=82, y=142)

        def loading():
            self.labelExport = tk.Label(self)
            self.labelExport.place(x=100, y=150)
            runexport1 = threading.Thread(
                name='Export', target=bluetoothexport)
            runexport1.start()

            for i in range(5):
                print(i)
                self.labelExport.config(image=photos_ex1)
                root.update_idletasks()
                time.sleep(1)
                self.labelExport.config(image=photos_ex2)
                root.update_idletasks()
                time.sleep(1)
                self.labelExport.config(image=photos_ex3)
                root.update_idletasks()
                time.sleep(1)
                print('loading(): '), channel
                if i == 4 or channel == -1:
                    self.labelExport.place_forget()
                    break

        def exportok():
            btn1.config(state='normal')
            btn2.config(state='normal')
            btn3.config(state='normal')

            self.label5.place_forget()
            self.labelExport.place_forget()
            self.btnExport.place_forget()

        def btn11(*args):
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            btn1.config(image=photo055)
            # bluetoothexport

        def btn111(*args):
            btn1.config(image=photo019)

            runexport = threading.Thread(name='Export', target=loading)
            runexport.start()

        def btn22(*args):
            btn1.config(state='disabled')
            btn3.config(state='disabled')
            btn2.config(image=photos156)

            """self.label1 = tk.Label(self,padx=143,pady=49,bg='#D9D9D9')
                        self.label1.place(x=10,y=90)
                        self.label2 = tk.Label(
                            self,padx=143,pady=24,bg='#262626')
                        self.label2.place(x=10,y=90)
                        self.label3 = tk.Label(
                            self,text='你確定要永久刪除這些檔案嗎?',fg='white',bg='#262626',font="Arial 14")
                        self.label3.place(x=30,y=105)"""
            self.label1 = tk.Label(self, image=photos172)
            self.label1.place(x=100, y=150)
            self.btn44 = tk.Button(self, image=photo026,
                                   highlightthickness=0, bd=0, command=btn44)
            self.btn44.place(x=200, y=300)  # enter
            self.btn55 = tk.Button(self, image=photos159,
                                   highlightthickness=0, bd=0, command=btn55)
            self.btn55.place(x=430, y=300)  # cancel

            self.btn44.bind('<Button-1>', btn44)
            self.btn44.bind("<ButtonRelease-1>", btn444)
            self.btn55.bind('<Button-1>', btn55)
            self.btn55.bind("<ButtonRelease-1>", btn555)

        def btn222(*args):
            btn1.config(state='normal')
            btn2.config(image=photos155)
            btn3.config(state='normal')

        def btn33(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(image=photo042)

        def btn333(*args):
            controller.switch_frame(File)

        def sqlitRemove():
            conn = sqlite3.connect(
                'C:/Users/USER/Desktop/convenience/TEST2.db')
            conn.execute("DELETE FROM TEST2")
            conn.commit()
            conn.close()

        def btn44(*args):
            self.btn44.config(image=photo057)
            self.btn44.config(state='disabled')

            # date remove
            self.clearData = tk.Label(self, image=photos37)
            self.clearData.place(x=2, y=85)
            Remove = threading.Thread(name='Remove', target=sqlitRemove)
            Remove.start()

        def btn444(*args):
            btn1.config(state='normal')
            btn3.config(state='normal')
            self.btn44.config(image=photo026)
            self.label1.place_forget()
            self.btn44.place_forget()
            self.btn55.place_forget()
            time.sleep(2)
            self.clearData.place_forget()

        def btn55(*args):
            self.btn55.config(image=photos160)

        def btn555(*args):
            self.btn44.config(image=photos159)
            self.label1.place_forget()
            # self.label2.place_forget()
            # self.label3.place_forget()
            self.btn44.place_forget()
            self.btn55.place_forget()

        btn1 = tk.Button(self, image=photo019, highlightthickness=0, bd=0)
        btn2 = tk.Button(self, image=photos155, highlightthickness=0, bd=0)
        btn3 = tk.Button(self, image=photo006, highlightthickness=0, bd=0)
        btn1.place(x=100, y=200)  # 匯出
        btn2.place(x=100, y=350)  # 刪除
        btn3.place(x=550, y=350)  # 返回

        btn1.bind('<Button-1>', btn11)
        btn1.bind("<ButtonRelease-1>", btn111)
        btn2.bind('<Button-1>', btn22)
        btn2.bind("<ButtonRelease-1>", btn222)
        btn3.bind('<Button-1>', btn33)
        btn3.bind("<ButtonRelease-1>", btn333)

        year1, month1, date1, hour1, minute1 = read_time()
        self.label12 = tk.Label(self, text=year1, font=1)
        self.label12.place(x=10, y=5)
        self.label13 = tk.Label(self, text=month1, font=1)
        self.label13.place(x=60, y=5)
        self.label14 = tk.Label(self, text=date1, font=1)
        self.label14.place(x=88, y=5)
        self.label15 = tk.Label(self, text=hour1, font=1)
        self.label15.place(x=138, y=5)
        self.label16 = tk.Label(self, text=minute1, font=1)
        self.label16.place(x=165, y=5)
        self.update()

    def update(self):
        year1, month1, date1, hour1, minute1 = read_time()
        self.label12.config(text=year1 + '-')
        self.label13.config(text=month1 + '-')
        self.label14.config(text=date1)
        self.label15.config(text=hour1 + ':')
        self.label16.config(text=minute1)
        self.after(1000, self.update)


class File(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        conn = sqlite3.connect('C:/Users/USER/Desktop/convenience/TEST2.db',
                               check_same_thread=False)  # 避免線程問題
        cursor = conn.cursor()  # 呼叫要使用
        conn.text_factory = str  # 8-bit取代unicode-string
        print("Opened database successfully")
        #w, h = root.winfo_screenwidth(), root.winfo_screenheight()  # 獲取窗口高度寬度，還是分辨率，不確定
        #print("窗口高度 寬度")

        testtype = str(testtype_read())
        resulttype = resulttype_read()
        todaytime = time_read()

        def topLevel(seltext):  # Hi,I'm mini window XD.

            def back():
                top.destroy()

            def startpage():
                top.destroy()
                controller.switch_frame(StartPage)

            def BTprint():
                os.system("sudo sh blue.sh")  # 連接藍芽?
                try:
                    btn1.config(state='disabled')
                    btn2.config(state='disabled')
                    btn3.config(state='disabled')
                    subprocess.call("sudo /etc/init.d/cups restart".split())
                    subprocess.call("sudo /etc/init.d/bluetooth start".split())

                    print("cross line2")

                    f1 = codecs.open(
                        "C:/Users/USER/Desktop/convenience/Firstep/Print_file.txt", "r", encoding='utf-8')

                    f2 = codecs.open(
                        "C:/Users/USER/Desktop/convenience/bluePrinter.txt", "r", encoding='utf-8')

                    text = f1.readlines()
                    addr = f2.readline()
                    f2.close()
                    print(f1)
                    print("In Print state ------------------------Do Print")
                    # print "讀取文檔後Address:" , addr
                    bd_addr = addr
                    port = 1
                    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                    sock.connect((bd_addr, port))
                    print("內容顯示:")
                    for result in text:
                        # result = repr(result)  # 將任意值轉為字串，適合閱讀器(機器)閱讀
                        # result = result.strip("'\ufeff'")  # 去除ufeff
                        # print(result)
                        # result = unicode(result, 'big5')

                        # result = result.decode('unicode-escape')
                        sock.send(result.encode('big5'))
                        # sock.send(result.encode('GB18030'))
                    sock.send('\n\n\n\n')
                    sock.close()
                    print(result)
                    print("Print successful")
                    # var2.set("打印成功")
                    top.label5 = tk.Label(top, image=photos177)  # 列印成功
                    top.label5.place(x=2, y=85)
                    top.printOK = tk.Button(
                        top, image=photo026, command=printprocess1)  # 列印成功確認鍵
                    top.printOK.place(x=82, y=142)

                except:
                    btn1.config(state='disabled')
                    btn2.config(state='disabled')
                    btn3.config(state='disabled')
                    print("Print fail")
                    # var2.set("打印失败")
                    top.label5 = tk.Label(top, image=photos178)
                    top.label5.place(x=100, y=150)
                    top.printOK = tk.Button(
                        top, image=photo026, command=printprocess1)
                    top.printOK.place(x=315, y=300)

            def loading2():
                print("loading2")
                top.label4 = tk.Label(top, image=photos36)
                top.label4.place(x=100, y=150)

            def printing():
                print("print-------------------------------------------------------------------------------------------------------------------------------------")
                threading.Thread(
                    name='Print', target=BTprint).start()
                loading2()

            def printprocess1():
                btn1.config(state='normal')
                btn2.config(state='normal')
                btn3.config(state='normal')
                btn4.config(state='normal')
                top.label4.place_forget()
                top.label5.place_forget()
                top.printOK.place_forget()

            top = tk.Toplevel()
            top.geometry("800x600")
            # top.geometry('200x100')
            #top.attributes("-fullscreen", True)
            # top.config(cursor='none')
            cursor = conn.execute("SELECT * from TEST2")

            w, h = 320, 240
            w, h = top.winfo_screenwidth(), top.winfo_screenheight()
            # top.overrideredirect(1)  # 視窗邊框消失
            #top.geometry("%dx%d+0+0" % (w, h))

            top.focus_set()
            # top.config(cursor="none")

            # 選取檔案後的頁面

            label2 = tk.Label(top, font="Courier 28")
            label2.place(x=10, y=30)
            label3 = tk.Label(top, font="Courier 28")
            label3.place(x=10, y=70)

            label5 = tk.Label(top, font="Courier 28", text="受測者編碼(ID):")
            label5.place(x=10, y=110)
            label6 = tk.Label(top, font="Courier 28")
            label6.place(x=310, y=110)
            label7 = tk.Label(top, font="Courier 28", text="品項:")
            label7.place(x=10, y=160)
            label8 = tk.Label(top, font="Courier 28")
            label8.place(x=130, y=160)
            label9 = tk.Label(top, font="Courier 28", text=" ")
            label9.place(x=10, y=260)
            label10 = tk.Label(top, font="Courier 28")
            label10.place(x=180, y=260)
            label11 = tk.Label(top, font="Courier 28", text="MET:")
            label11.place(x=10, y=360)
            label12 = tk.Label(top, font="Courier 28")
            label12.place(x=130, y=360)
            label13 = tk.Label(top, font="Courier 28", text="MOR:")
            label13.place(x=10, y=460)
            label14 = tk.Label(top, font="Courier 28")
            label14.place(x=130, y=460)


            def btn11(*args):
                btn2.config(state='disabled')
                btn3.config(state='disabled')
                btn4.config(state='disabled')
                btn1.config(image=photo056)

            def btn111(*args):
                btn1.config(image=photo015)
                btn1.config(state='disabled')
                printing()  # -------------------------------------------------------------------------------printing

            def btn22(*args):
                btn1.config(state='disabled')
                btn2.config(state='disabled')
                btn3.config(state='disabled')
                btn4.config(state='disabled')
                btn2.config(image=photos170)

            def btn222(*args):
                btn2.config(image=photos169)
                runexport = threading.Thread(name='Export', target=loading)
                runexport.start()

            def btn33(*args):
                btn1.config(state='disabled')
                btn2.config(state='disabled')
                # btn3.config(state='disabled')
                btn4.config(state='disabled')
                btn3.config(image=photo042)

            def btn333(*args):
                btn3.config(image=photo057)
                back()

            def btn44(*args):
                btn1.config(state='disabled')
                btn2.config(state='disabled')
                # btn4.config(state='disabled')
                btn3.config(state='disabled')
                btn4.config(image=photo041)

            def btn444(*args):
                btn4.config(image=photo005)
                startpage()

            def bluetoothexport():
                f = open("C:/Users/USER/Desktop/convenience/blueStorage.txt", "r")
                s = f.readline()
                print("讀取文檔後Address:"), s
                f.close()
                os.system("sudo sh C:/Users/USER/Desktop/convenience/blue.sh")
                # cli = obexftp.client(obexftp.BLUETOOTH)
                global channel
                # channel = obexftp.browsebt(s, obexftp.PUSH)
                # it is the correct channel, I've doubled checked
                print('channel: '), channel
                if channel == -1:
                    print('失敗')
                    top.label5 = tk.Label(top, image=photos181)
                    top.label5.place(x=2, y=85)
                    top.btnExport = tk.Button(
                        top, image=photo026, highlightthickness=0, bd=0, command=exportok)
                    top.btnExport.place(x=82, y=142)

                else:
                    cursor = conn.execute("SELECT *  from TEST2")
                    print("---------Make Excel---------")
                    print("part 2 ")
                    f_exportxls = 'C:/Users/USER/Desktop/convenience/'+seltext+'.xls'
                    w = xlwt.Workbook()
                    w = xlwt.Workbook(encoding='utf-8')  # 使excel輸出中文
                    t = w.add_sheet(
                        'data', cell_overwrite_ok=True)  # 添加一個sheet
                    t.write(0, 0, 'No.')  # 開始寫入數據
                    t.write(0, 1, "受測者編碼")
                    # t.write(0,2,"Patient's ID")
                    t.write(0, 2, 'Item')
                    t.write(0, 3, 'c線判斷')  # c_line
                    t.write(0, 5, '陰陽性判斷_T1')
                    t.write(0, 7, '陰陽性判斷_T2')
                    t.write(0, 9, '實際數據值_T1')
                    t.write(0, 11, '實際數據值_T2')
                    # t.write(0,4,'Cutoff')
                    t.write(0, 13, 'Time')

                    for row in cursor:  # Later fix.
                        #selectrow = ' '+row[6]
                        selectrow = row[6]
                        print('selectrow: ', selectrow, ' seltext: ', seltext)

                        if (selectrow == seltext):
                            print('Same!')
                            print('Test Type row[2]: ', row[2])

                            if row[2] == 1:
                                print('Result Type row[1]: ', row[1])
                                t.write(1, 0, str(row[0]))  # No.
                                t.write(1, 1, row[3])  # id
                                t.write(1, 2, row[7])  # A_item
                                t.write(1, 3, row[8])  # c_line
                                t.write(1, 5, row[9])  # A_RESULT_T1
                                t.write(1, 7, row[10])  # A_RESULT_T2
                                t.write(1, 9, row[11])  # Impedance_T1
                                t.write(1, 11, row[12])  # Impedance_T2
                                t.write(1, 13, row[4])   # time

                            elif row[2] == 2:
                                print('Result Type row[1]: ', row[1])
                                t.write(1, 0, str(row[0]))  # No.
                                t.write(1, 1, row[3])  # id
                                t.write(1, 2, row[7])  # A_item
                                t.write(1, 3, row[8])  # c_line
                                t.write(1, 5, row[9])  # A_RESULT_T1
                                t.write(1, 7, row[10])  # A_RESULT_T2
                                t.write(1, 9, row[11])  # Impedance_T1
                                t.write(1, 11, row[12])  # Impedance_T2
                                t.write(1, 13, row[4])   # time

                                # t.write(insertnum, 0, str(row[0]))  # No.
                                # t.write(insertnum, 1, row[3])  # id
                                # t.write(insertnum, 2, row[7])  # A_item
                                # t.write(insertnum, 3, row[8])  # c_line
                                # t.write(insertnum, 5, row[9])  # A_RESULT_T1
                                # t.write(insertnum, 7, row[10])  # A_RESULT_T2
                                # t.write(insertnum, 9, row[11])  # Impedance_T1
                                # t.write(insertnum, 11, row[12])  # Impedance_T2
                                # t.write(insertnum, 13, row[4])   # time

                                t.write(2, 0, str(row[0]))  # No.
                                t.write(2, 1, row[3])  # id
                                t.write(2, 2, row[7])  # A_item
                                t.write(2, 3, row[8])  # A_RESULT_T1
                                t.write(2, 5, row[9])  # A_RESULT_T1
                                t.write(2, 7, row[10])  # A_RESULT_T2
                                t.write(2, 9, row[11])  # Impedance_T1
                                t.write(2, 11, row[12])  # Impedance_T2
                                t.write(2, 13, row[4])   # time
                            elif row[2] == 3:
                                print('Result Type row[1]: ', row[1])
                                t.write(1, 0, str(row[0]))  # No.
                                t.write(1, 1, row[3])  # id
                                t.write(1, 2, row[7])  # A_item
                                t.write(1, 3, row[8])  # c_line
                                t.write(1, 5, row[9])  # A_RESULT_T1
                                t.write(1, 7, row[10])  # A_RESULT_T2
                                t.write(1, 9, row[11])  # Impedance_T1
                                t.write(1, 11, row[12])  # Impedance_T2
                                t.write(1, 13, row[4])   # time

                                t.write(2, 0, str(row[0]))  # No.
                                t.write(2, 1, row[3])  # id
                                t.write(2, 2, row[7])  # A_item
                                t.write(2, 3, row[8])  # A_RESULT_T1
                                t.write(2, 5, row[9])  # A_RESULT_T1
                                t.write(2, 7, row[10])  # A_RESULT_T2
                                t.write(2, 9, row[11])  # Impedance_T1
                                t.write(2, 11, row[12])  # Impedance_T2
                                t.write(2, 13, row[4])   # time

                            break
                        else:
                            print('ERROR EXCEL!')

                    w.save(f_exportxls)

                    print("---------Make done---------")
                    time.sleep(3)
                    print("---------Sending---------")

                    print(s)
                    os.system('sdptool search --bdaddr '+s+' OPUSH')
                    os.system('obexftp --nopath --noconn --uuid none --bluetooth ' +
                              s+' --channel 12 --put ' + 'C:/Users/USER/Desktop/convenience/'+seltext+'.xls')  # 檔案名前面多了一個空格，自己注意

                    time.sleep(5)
                    print('成功')
                    top.label5 = tk.Label(top, image=photos185)
                    top.label5.place(x=2, y=85)
                    top.btnExport = tk.Button(
                        top, image=photo026, command=exportok)
                    top.btnExport.place(x=82, y=142)

            def loading():
                top.labelExport = tk.Label(top)
                top.labelExport.place(x=100, y=150)
                runexport1 = threading.Thread(
                    name='Export', target=bluetoothexport)
                runexport1.start()

                for i in range(5):
                    print(i)
                    top.labelExport.config(image=photos_ex1)
                    root.update_idletasks()
                    time.sleep(1)
                    top.labelExport.config(image=photos_ex2)
                    root.update_idletasks()
                    time.sleep(1)
                    top.labelExport.config(image=photos_ex3)
                    root.update_idletasks()
                    time.sleep(1)
                    print('loading(): '), channel
                    if i == 4 or channel == -1:
                        top.labelExport.place_forget()
                        break

            def exportok():
                btn1.config(state='normal')
                btn2.config(state='normal')
                btn3.config(state='normal')
                btn4.config(state='normal')

                top.label5.place_forget()
                top.labelExport.place_forget()
                top.btnExport.place_forget()

            btn1 = tk.Button(top, image=photo015, highlightthickness=0, bd=0)
            btn2 = tk.Button(top, image=photos169, highlightthickness=0, bd=0)
            btn3 = tk.Button(top, image=photo006, highlightthickness=0, bd=0)
            btn4 = tk.Button(top, image=photo005, highlightthickness=0, bd=0)

            btn1.place(x=550, y=50)  # ------列印
            btn2.place(x=550, y=180)  # ------匯出
            btn3.place(x=550, y=310)  # ------返回
            btn4.place(x=550, y=440)  # ------首頁

            btn1.bind('<Button-1>', btn11)
            btn1.bind("<ButtonRelease-1>", btn111)
            btn2.bind('<Button-1>', btn22)
            btn2.bind("<ButtonRelease-1>", btn222)
            btn3.bind('<Button-1>', btn33)
            btn3.bind("<ButtonRelease-1>", btn333)
            btn4.bind('<Button-1>', btn44)
            btn4.bind("<ButtonRelease-1>", btn444)
#####
            for row in cursor:
                #selectrow = ' '+row[6]
                selectrow = row[6]
                if (selectrow == seltext):
                    print(selectrow)
                    # print cursor.fetchall()
                    print('test type row[2]: ', row[2])
                    print('result type row[1]: ', row[1])
                    if row[2] == 1:
                        print("第一列為1")

                        file_name = row[6]
                        timedata = row[4]
                        ID = row[3]
                        A_item = row[7]
                        c_line = row[8]
                        #A_RESULT = row[9]
                        Impedance_T1 = row[11]
                        Impedance_T2 = row[12]

                        label2.config(text=file_name)
                        label3.config(text=timedata)
                        label6.config(text=ID)
                        label8.config(text=A_item)
                        label10.config(text=c_line)
                        label12.config(text=Impedance_T1)
                        label14.config(text=Impedance_T2)

                    elif row[2] == 2:
                        print("第二列為2")

                        file_name = row[6]
                        timedata = row[4]
                        ID = row[3]
                        A_item = row[7]
                        c_line = row[8]
                        #A_RESULT = row[9]
                        Impedance_T1 = row[11]
                        Impedance_T2 = row[12]

                        label2.config(text=file_name)
                        label3.config(text=timedata)
                        label6.config(text=ID)
                        label8.config(text=A_item)
                        label10.config(text=c_line)
                        label12.config(text=Impedance_T1)
                        label14.config(text=Impedance_T2)

                    elif row[2] == 3:
                        print("第二列為3")

                        file_name = row[6]
                        timedata = row[4]
                        ID = row[3]
                        A_item = row[7]
                        c_line = row[8]
                        #A_RESULT = row[9]
                        Impedance_T1 = row[11]
                        Impedance_T2 = row[12]

                        label2.config(text=file_name)
                        label3.config(text=timedata)
                        label6.config(text=ID)
                        label8.config(text=A_item)
                        label10.config(text=c_line)
                        label12.config(text=Impedance_T1)
                        label14.config(text=Impedance_T2)

            #year1, month1, date1, hour1, minute1 = read_time()
            top.label12 = tk.Label(top, text="2023" + '-', font=1)
            top.label13 = tk.Label(top, text="09" + '-', font=1)
            top.label14 = tk.Label(top, text="27", font=1)
            top.label15 = tk.Label(top, text="15" + ':', font=1)
            top.label16 = tk.Label(top, text="51", font=1)

            top.label12.place(x=10, y=5)
            top.label13.place(x=60, y=5)
            top.label14.place(x=88, y=5)
            top.label15.place(x=138, y=5)
            top.label16.place(x=165, y=5)
            #top.update()

        def keyboardshow():
            global inputtxt
            inputtxt = 3
            controller.switch_frame(keyboard)

        def keyboardshow2():
            global inputtxt
            inputtxt = 9
            controller.switch_frame(keyboard)

        def startpage():
            btn11.config(state='disabled')
            btn12.config(state='disabled')
            btn13.config(state='disabled')
            controller.switch_frame(StartPage)

        def get_list(event):
            # showcase
            # get selected line index
            index = listbox1.curselection()[0]
            print('index:', index)
            # get the line's text
            seltext = listbox1.get(index)
            print('seltext: ', seltext)
            id = 'ID'
            if machine_number in seltext:
                # showcase(seltext)
                # print(machine_number, ',', id, ',', seltext)
                printprocess()  # -------------------------------------------------------------------------------------------------print
                topLevel(seltext)  # into mini window :)

        def printprocess():
            index = listbox1.curselection()[0]
            # get the line's text
            seltext = listbox1.get(index)
            print('printprocess(): ', seltext)
            cursor = conn.execute("SELECT * from TEST2")
            for row in cursor:
                selectrow = row[6]
                if selectrow == seltext:
                    print('row[2]: ', row[2])

                    # 待修，看最後要的列印內容是什麼
                    if row[2] == 1:
                        Print1 = ' 機碼 :'+machine_number.strip()+'\n'+' 測試時間 :'+row[4].strip()+'\n'+' 受測者編碼 :'+row[3].strip()+'\n'+' 品項 :'+row[7].strip(
                        )+'\n'+' c線數值 :'+row[8].strip()+'\n'+' T1檢測值 :'+row[9].strip()+'\n'+' T2檢測值 :'+row[10].strip()+'\n'+' '+'--------------------------------'+'\n'+' 列印時間 :' + todaytime
                        f_Print1 = open(
                            "C:/Users/USER/Desktop/convenience/Firstep/Print_file.txt", "w")
                        f_Print1.write(Print1)
                        f_Print1.close()
                        print(Print1)
                    elif row[2] == 2:
                        print("456")
                        Print2 = ' 機碼 :'+machine_number.strip()+'\n'+' 測試時間 :'+row[4].strip()+'\n'+' 受測者編碼 :'+row[3].strip()+'\n'+' 品項 :'+row[7].strip(
                        )+'\n'+' c線數值 :'+row[8].strip()+'\n'+' T1檢測值 :'+row[9].strip()+'\n'+' T2檢測值 :'+row[10].strip()+'\n'+' '+'--------------------------------'+'\n'+' 列印時間 :' + todaytime
                        f_Print2 = open(
                            "C:/Users/USER/Desktop/convenience/Firstep/Print_file.txt", "w")
                        f_Print2.write(Print2)
                        f_Print2.close()
                        print(Print2)
                    elif row[2] == 3:
                        print("456")
                        Print3 = ' 機碼 :'+machine_number.strip()+'\n'+' 測試時間 :'+row[4].strip()+'\n'+' 受測者編碼 :'+row[3].strip()+'\n'+' 品項 :'+row[7].strip(
                        )+'\n'+' c線數值 :'+row[8].strip()+'\n'+' T1檢測值 :'+row[9].strip()+'\n'+' T2檢測值 :'+row[10].strip()+'\n'+' '+'--------------------------------'+'\n'+' 列印時間 :' + todaytime
                        f_Print3 = open(
                            "C:/Users/USER/Desktop/convenience/Firstep/Print_file.txt", "w")
                        f_Print3.write(Print3)
                        f_Print3.close()
                        print(Print3)

        def PageDown():
            listbox1.yview_scroll(12, "units")

        def PageUP():
            listbox1.yview_scroll(-12, "units")

        # create the listbox (note that size is in characters)
        listbox1 = tk.Listbox(self, font="Courier 28",
                              bg='white', width=23, height=13)
        listbox1.place(x=9, y=40)
        cursor = conn.execute("SELECT *  from TEST2")
        for row in cursor:
            print(row[5])
            #item_1 = ' '+row[6]
            item_1 = row[6]
            item_2 = '  ID :'+row[3]
            item_3 = row[5]
            # 資料庫排序由新至舊
            listbox1.insert(0, '')
            listbox1.insert(0, item_2)
            listbox1.insert(0, item_1)
            if '月' in row[5]:
                listbox1.insert(0, '')
                listbox1.insert(0, item_3)

            # 資料庫排序由舊至新(舊版寫法)
            #    listbox1.insert(0, '')
            # if '月' in row[5]:
                #listbox1.insert(tk.END, '')
                #listbox1.insert(tk.END, item_3)
                #listbox1.insert(tk.END, '')
            #listbox1.insert(tk.END, item_1)
            #listbox1.insert(tk.END, item_2)
            #listbox1.insert(tk.END, '')

        listbox1.bind('<ButtonRelease-1>', get_list)  # GOGO~ Exciting~~

        def btn333(*args):
            btn11.config(state='disabled')
            btn12.config(state='disabled')
            btn14.config(state='disabled')
            btn15.config(state='disabled')
            btn13.config(image=photo042)

        def btn3333(*args):
            btn13.config(state='disabled')
            btn13.config(image=photo006)
            controller.switch_frame(StartPage)

        def btn222(*args):
            btn11.config(state='disabled')
            btn13.config(state='disabled')
            btn14.config(state='disabled')
            btn15.config(state='disabled')
            btn12.config(image=photo041)

        def btn2222(*args):
            btn12.config(state='disabled')
            btn12.config(image=photo005)
            controller.switch_frame(StartPage)

        def btn111(*args):
            btn12.config(state='disabled')
            btn13.config(state='disabled')
            btn14.config(state='disabled')
            btn15.config(state='disabled')
            btn11.config(image=photos158)

        def btn1111(*args):
            btn11.config(state='disabled')
            btn11.config(image=photos157)
            # BluetoothExport and ClearData page.
            controller.switch_frame(BluetoothExport)

        btn11 = tk.Button(self, image=photos157,
                          highlightthickness=0, bd=0)  # command=exportusb
        btn12 = tk.Button(self, image=photo005,
                          highlightthickness=0, bd=0, command=StartPage)
        btn13 = tk.Button(self, image=photo006,
                          highlightthickness=0, bd=0, command=StartPage)
        btn14 = tk.Button(self, image=photo024,
                          highlightthickness=0, bd=0, command=PageUP)
        btn15 = tk.Button(self, image=photo025,
                          highlightthickness=0, bd=0, command=PageDown)

        btn11.place(x=550, y=310)  # ------更多
        # btn12.place(x=13, y=48)  # ------首頁
        btn13.place(x=550, y=440)  # ------返回
        # btn13.grid()
        btn14.place(x=550, y=50)  # ------上一頁
        btn15.place(x=550, y=180)  # ------下一頁

        btn11.bind('<Button-1>', btn111)
        btn11.bind("<ButtonRelease-1>", btn1111)
        btn12.bind('<Button-1>', btn222)
        btn12.bind("<ButtonRelease-1>", btn2222)
        btn13.bind('<Button-1>', btn333)
        btn13.bind("<ButtonRelease-1>", btn3333)

        # label2 = tk.Label(self,image=photo14)
        # label2.place(x=230,y=1)

        #year1, month1, date1, hour1, minute1 = read_time()
        #self.label12 = tk.Label(self, text=year1, font=1)
        #self.label12.place(x=10, y=5)
        #self.label13 = tk.Label(self, text=month1, font=1)
        #self.label13.place(x=60, y=5)
        #self.label14 = tk.Label(self, text=date1, font=1)
        #self.label14.place(x=88, y=5)
        #self.label15 = tk.Label(self, text=hour1, font=1)
        #self.label15.place(x=138, y=5)
        #self.label16 = tk.Label(self, text=minute1, font=1)
        #self.label16.place(x=165, y=5)
        #self.update()

        #year1, month1, date1, hour1, minute1 = read_time()
        self.label12 = tk.Label(self, text="2023", font=1)
        self.label12.place(x=10, y=5)
        self.label13 = tk.Label(self, text="09", font=1)
        self.label13.place(x=60, y=5)
        self.label14 = tk.Label(self, text="27", font=1)
        self.label14.place(x=88, y=5)
        self.label15 = tk.Label(self, text="15", font=1)
        self.label15.place(x=138, y=5)
        self.label16 = tk.Label(self, text="51", font=1)
        self.label16.place(x=165, y=5)
        self.update()

    def update(self):
        #year1, month1, date1, hour1, minute1 = read_time()
        self.label12.config(text="2023" + '-')
        self.label13.config(text="09" + '-')
        self.label14.config(text="27")
        self.label15.config(text="15" + ':')
        self.label16.config(text="51")
        self.after(1000, self.update)


class Setting(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, height="320", width="480")
        #   R202_version = tk.Label(self,text='版本 : 1.0.0',font='Courier 15')
        # R202_version.place(x=7,y=430)

        def settime():
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            # btn3.config(state='disabled')
            btn4.config(state='disabled')
            # btn5.config(state='disabled')
            # btn6.config(state='disabled')
            # controller.show_frame(Settime)

        def startpage():
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            # btn3.config(state='disabled')
            btn4.config(state='disabled')
            # btn5.config(state='disabled')
            # btn6.config(state='disabled')
            controller.switch_frame(StartPage)

        # def save():
            # btn1.config(state='disabled')
            # btn2.config(state='disabled')
            # btn3.config(state='disabled')
            # btn4.config(state='disabled')
            # btn5.config(state='disabled')
            # btn6.config(state='disabled')
            # self.btn7 = tk.Button(self, image=photo023, command=saveok)
            # self.btn7.grid(row=0, column=0,padx=58,pady=180)

        def btn66(*args):

            btn1.config(state='disabled')
            btn2.config(state='disabled')
            # btn3.config(state='disabled')
            btn4.config(state='disabled')
            btn5.config(state='disabled')
            btn6.config(image=photo042)

        def btn666(*args):
            btn6.config(state='disabled')
            btn6.config(image=photo006)
            controller.switch_frame(StartPage)

        def btn55(*args):

            btn1.config(state='disabled')
            btn2.config(state='disabled')
            # btn3.config(state='disabled')
            btn4.config(state='disabled')
            btn6.config(state='disabled')
            btn5.config(image=photo041)

        def btn555(*args):
            btn5.config(state='disabled')
            btn5.config(image=photo005)
            controller.switch_frame(StartPage)

        def btn44(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            # btn3.config(state='disabled')
            btn5.config(state='disabled')
            btn6.config(state='disabled')
            btn4.config(image=photo058)

        def btn444(*args):
            btn4.config(state='disabled')
            btn4.config(image=photo027)
            # ----------------------------------bluetoothPrinter
            controller.switch_frame(OneofThree)

        # def btn33(*args):

            # btn1.config(state='disabled')
            # btn2.config(state='disabled')
            # btn4.config(state='disabled')
            # btn5.config(state='disabled')
            # btn6.config(state='disabled')
            # btn3.config(image=photo045)

        # def btn333(*args):
            # btn3.config(state='disabled')
            # btn3.config(image=photo009)
           # btupdate()  # --------------------------------------------------btupdate

        def btn11(*args):

            btn2.config(state='disabled')
            # btn3.config(state='disabled')
            btn4.config(state='disabled')
            btn5.config(state='disabled')
            btn6.config(state='disabled')
            btn1.config(image=photo043)

        def btn111(*args):
            btn1.config(state='disabled')
            btn1.config(image=photo007)
            controller.switch_frame(Settime)

        btn1 = tk.Button(self, image=photo007,
                         highlightthickness=0, bd=0, command=Settime)
        btn2 = tk.Button(self, image=photo008, highlightthickness=0, bd=0)
        # btn3 = tk.Button(self, image=photo009, highlightthickness=0,bd=0)

        btn4 = tk.Button(self, image=photo027, highlightthickness=0, bd=0)
        btn5 = tk.Button(self, image=photo005,
                         highlightthickness=0, bd=0, command=startpage)
        btn6 = tk.Button(self, image=photo006,
                         highlightthickness=0, bd=0, command=startpage)

        # btn1.pack(pady=50)
        # btn4.pack(pady=50)

        # btn6.pack(anchor=E)
        btn1.place(x=100, y=200)  # -----時間設置
        # btn3.place(x=56,y=150)                  #-----軟體更新
        btn4.place(x=100, y=350)  # -----藍芽
        # btn5.place(x=113,y=418)                 #-----首頁
        btn6.place(x=550, y=350)  # -----返回

        btn1.bind('<Button-1>', btn11)
        btn1.bind("<ButtonRelease-1>", btn111)
        # btn3.bind('<Button-1>', btn33)
        # btn3.bind("<ButtonRelease-1>", btn333)
        btn4.bind('<Button-1>', btn44)
        btn4.bind("<ButtonRelease-1>", btn444)
        btn5.bind('<Button-1>', btn55)
        btn5.bind("<ButtonRelease-1>", btn555)
        btn6.bind('<Button-1>', btn66)
        btn6.bind("<ButtonRelease-1>", btn666)

        # label2 = tk.Label(self,image=photo14)
        # label2.place(x=230,y=1)

        year1, month1, date1, hour1, minute1 = read_time()
        self.label12 = tk.Label(self, text=year1, font=1)
        self.label12.place(x=10, y=5)
        self.label13 = tk.Label(self, text=month1, font=1)
        self.label13.place(x=60, y=5)
        self.label14 = tk.Label(self, text=date1, font=1)
        self.label14.place(x=88, y=5)
        self.label15 = tk.Label(self, text=hour1, font=1)
        self.label15.place(x=138, y=5)
        self.label16 = tk.Label(self, text=minute1, font=1)
        self.label16.place(x=165, y=5)
        self.update()

    def update(self):
        year1, month1, date1, hour1, minute1 = read_time()
        self.label12.config(text=year1 + '-')
        self.label13.config(text=month1 + '-')
        self.label14.config(text=date1)
        self.label15.config(text=hour1 + ':')
        self.label16.config(text=minute1)
        self.after(1000, self.update)


class OneofThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def btn11(*args):
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            btn4.config(state='disabled')

            btn1.config(image=photos166)

        def btn111(*args):
            btn1.config(state='disabled')
            btn1.config(image=photos165)
            controller.switch_frame(bluePrinter)

        # def btn22(*args):
        #     btn1.config(state='disabled')
        #     btn3.config(state='disabled')
        #     btn4.config(state='disabled')

        #     btn2.config(image=photo058)

        # def btn222(*args):
        #     btn2.config(state='disabled')
        #     btn2.config(image=photo027)
        #     controller.switch_frame(Setting)

        def btn33(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn4.config(state='disabled')

            btn3.config(image=photos168)

        def btn333(*args):
            btn3.config(state='disabled')
            btn3.config(image=photos167)
            controller.switch_frame(blueStorage)

        def btn44(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            btn4.config(image=photo042)

        def btn444(*args):
            btn4.config(state='disabled')
            btn4.config(image=photo006)
            controller.switch_frame(Setting)

        btn1 = tk.Button(self, image=photos165, highlightthickness=0, bd=0)
        btn2 = tk.Button(self, image=photo027, highlightthickness=0, bd=0)
        btn3 = tk.Button(self, image=photos167, highlightthickness=0, bd=0)
        btn4 = tk.Button(self, image=photo006, highlightthickness=0, bd=0)

        btn1.place(x=100, y=200)  # bluePrinter
        # btn2.place(x=60,y=100)#blueScanner
        btn3.place(x=100, y=350)  # ------blueStorage  搜尋頁面
        btn4.place(x=550, y=350)  # ------返回

        btn1.bind('<Button-1>', btn11)
        btn1.bind("<ButtonRelease-1>", btn111)
        # btn2.bind('<Button-1>', btn22)
        # btn2.bind("<ButtonRelease-1>", btn222)
        btn3.bind('<Button-1>', btn33)
        btn3.bind("<ButtonRelease-1>", btn333)
        btn4.bind('<Button-1>', btn44)
        btn4.bind("<ButtonRelease-1>", btn444)

        year1, month1, date1, hour1, minute1 = read_time()
        self.label12 = tk.Label(self, text=year1, font=1)
        self.label12.place(x=10, y=5)
        self.label13 = tk.Label(self, text=month1, font=1)
        self.label13.place(x=60, y=5)
        self.label14 = tk.Label(self, text=date1, font=1)
        self.label14.place(x=88, y=5)
        self.label15 = tk.Label(self, text=hour1, font=1)
        self.label15.place(x=138, y=5)
        self.label16 = tk.Label(self, text=minute1, font=1)
        self.label16.place(x=165, y=5)
        self.update()

    def update(self):
        year1, month1, date1, hour1, minute1 = read_time()
        self.label12.config(text=year1 + '-')
        self.label13.config(text=month1 + '-')
        self.label14.config(text=date1)
        self.label15.config(text=hour1 + ':')
        self.label16.config(text=minute1)
        self.after(1000, self.update)


class bluePrinter(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        os.system('sudo rfkill unblock bluetooth')

        def scanner():
            lb.delete(0, 'end')
            try:

                var2.set("搜尋中...")
                root.update_idletasks()

                print("In Scanner state------------------------")
                a = []
                b = []
                global match
                nearby_devices = bluetooth.discover_devices(lookup_names=True)
                print("****found %d devices****" % len(nearby_devices))
                for addr, name in nearby_devices:
                    print("  %s - %s" % (addr, name))
                    a.append(addr)
                    b.append(name)
                    lb.insert('end', name)

                child = pexpect.spawn('bluetoothctl')
                child.expect('\# ')
                time.sleep(1)
                child.sendline('agent on')
                child.sendline('quit')
                time.sleep(1)
                print("a index:", a)
                print("b index:", b)
                match = dict(zip(b, a))
                print("match type:", type(match))
                print("match index:", match)
                print(match)
                btn1.config(state='normal')
                btn2.config(state='normal')
                btn3.config(state='normal')
                var2.set("搜尋完畢")

            except:
                var2.set("")
                self.label5 = tk.Label(self, image=photos186)
                self.label5.place(x=100, y=150)
                self.btn44 = tk.Button(self, image=photo026)
                self.btn44.place(x=315, y=300)
                self.btn44.bind('<Button-1>', btn444)
                # ------------------------------------------------------------------------------------------------------------
                self.btn44.bind("<ButtonRelease-1>", btn4444)

        def choice():
            try:
                var2.set("配對中...")
                root.update_idletasks()
                print("In Pair state ------------------------Do pairing")
                value = lb.get(lb.curselection())

                print("match index:"), match
                print("value: "), type(value)
                print("value index:"), value
                print("-----選擇的Addr-----")
                a = match.get(value)

                print("寫入文檔後Address:"), a
                f = open("C:/Users/USER/Desktop/convenience/bluePrinter.txt", "w")
                f.write(a)
                f.close()
                f = open("C:/Users/USER/Desktop/convenience//bluePrinter.txt", "r")
                s = f.readline()
                print("讀取文檔後Address:"), s
                f.close()

                subprocess.call("sudo systemctl restart bluetooth", shell=True)
                print("*****************************************************")
                subprocess.call(
                    "sudo chmod 777 /etc/cups/printers.conf", shell=True)

                s = s.replace(':', '')
                print("切開後冒號後顯示:"), s
                filea = open("/etc/cups/printers.conf", "r+")
                fileaString = filea.read()
                idFilter = 'bluetooth://'
                idPosition = fileaString.find(idFilter)
                filea.seek(idPosition+12, 0)
                filea.write(s)
                print("MAC address更改成功")
                filea.close()
                subprocess.call("sudo /etc/init.d/cups restart".split())
                print("CUPS restart")
                time.sleep(1)
                var2.set("配對成功")
            except:
                var2.set("配對失敗")

        def btn11(*args):
            btn2.config(state='disabled')
            btn3.config(state='disabled')

            btn1.config(image=photo059)

        def btn111(*args):
            btn1.config(state='disabled')
            btn1.config(image=photo028)
            scanner()

        def btn22(*args):
            btn1.config(state='disabled')
            btn3.config(state='disabled')

            btn2.config(image=photo060)

        def btn222(*args):
            btn2.config(state='disabled')
            btn2.config(image=photo029)
            choice()
            btn1.config(state='normal')
            btn2.config(state='normal')
            btn3.config(state='normal')

        def btn33(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(image=photo042)

        def btn333(*args):
            btn3.config(state='disabled')
            btn3.config(image=photo006)
            controller.switch_frame(OneofThree)

        def btn444(*args):
            self.btn44.config(image=photo057)

        def btn4444(*args):
            self.btn44.config(image=photo026)
            btn1.config(state='normal')
            btn2.config(state='normal')
            btn3.config(state='normal')
            self.btn44.place_forget()
            self.label5.place_forget()

        var1 = tk.StringVar()
        lb = tk.Listbox(self, width=36, height=6, bg='white',
                        listvariable=var1, font="Arial 28")
        lb.place(x=15, y=100)

        var2 = tk.StringVar()
        label1 = tk.Label(self, bg='gray', textvariable=var2,
                          width=35, height=1, font="Arial 28")
        label1.place(x=10, y=380)

        label3 = tk.Label(self, text='Bluetooth', font="Arial 28")
        label3.place(x=310, y=25)
        label4 = tk.Label(self, text='Device', font="Arial 28")
        label4.place(x=10, y=48)  # EN

        btn1 = tk.Button(self, image=photo028, highlightthickness=0, bd=0)
        btn2 = tk.Button(self, image=photo029, highlightthickness=0, bd=0)
        btn3 = tk.Button(self, image=photo006, highlightthickness=0, bd=0)

        btn1.place(x=110, y=450)  # ------尋找
        btn2.place(x=310, y=450)  # ------配對
        btn3.place(x=510, y=450)  # ------返回

        btn1.bind('<Button-1>', btn11)
        btn1.bind("<ButtonRelease-1>", btn111)
        btn2.bind('<Button-1>', btn22)
        btn2.bind("<ButtonRelease-1>", btn222)
        btn3.bind('<Button-1>', btn33)
        btn3.bind("<ButtonRelease-1>", btn333)

        year1, month1, date1, hour1, minute1 = read_time()
        self.label12 = tk.Label(self, text=year1, font=1)
        self.label12.place(x=10, y=5)
        self.label13 = tk.Label(self, text=month1, font=1)
        self.label13.place(x=60, y=5)
        self.label14 = tk.Label(self, text=date1, font=1)
        self.label14.place(x=88, y=5)
        self.label15 = tk.Label(self, text=hour1, font=1)
        self.label15.place(x=138, y=5)
        self.label16 = tk.Label(self, text=minute1, font=1)
        self.label16.place(x=165, y=5)
        self.update()

    def update(self):
        year1, month1, date1, hour1, minute1 = read_time()
        self.label12.config(text=year1 + '-')
        self.label13.config(text=month1 + '-')
        self.label14.config(text=date1)
        self.label15.config(text=hour1 + ':')
        self.label16.config(text=minute1)
        self.after(1000, self.update)


class blueStorage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        os.system('sudo rfkill unblock bluetooth')  # 打開藍芽

        def innerscan():
            print('-------------------Innerscan-------------------')
            os.system('bt-adapter -d')

        def scanner():
            lb.delete(0, 'end')
            try:

                var2.set("搜尋中...")
                root.update_idletasks()
                inscan = threading.Thread(name='inscan', target=innerscan)
                inscan.start()
                if inscan.is_alive():
                    print('inscan Still running.')
                else:
                    print('inscan Completed.')

                time.sleep(7)

                """child = pexpect.spawn("bluetoothctl")
                                child.send("scan on" + "\n")
                                for i in range(0, 10):
                                            print(i)
                                            time.sleep(1)"""

                print("In Scanner state------------------------")
                a = []
                b = []
                global match
                nearby_devices = bluetooth.discover_devices(lookup_names=True)
                print("****found %d devices****" % len(nearby_devices))
                for addr, name in nearby_devices:
                    print("  %s - %s" % (addr, name))
                    a.append(addr)
                    b.append(name)
                    lb.insert('end', name)

                child = pexpect.spawn('bluetoothctl')
                child.expect('\# ')
                time.sleep(1)
                child.sendline('agent on')
                child.sendline('quit')
                time.sleep(1)
                print("a index:"), a
                print("b index:"), b
                match = dict(zip(b, a))
                print("match type:"), type(match)
                print("match index:"), match
                print(match)
                btn1.config(state='normal')
                btn2.config(state='normal')
                btn3.config(state='normal')
                var2.set("搜尋完畢")

            except:
                var2.set("")
                self.label5 = tk.Label(self, image=photos186)
                self.label5.place(x=100, y=150)
                self.btn44 = tk.Button(self, image=photo026)
                self.btn44.place(x=315, y=300)
                self.btn44.bind('<Button-1>', btn444)
                self.btn44.bind("<ButtonRelease-1>", btn4444)

        def choice():
            try:
                var2.set("配對中...")
                root.update_idletasks()
                print("In Pair state ------------------------Do pairing")
                value = lb.get(lb.curselection())

                print("match index:"), match
                print("value: "), type(value)
                print("value index:"), value
                print("-----選擇的Addr-----")
                a = match.get(value)

                print("寫入文檔後Address:"), a
                f = open("C:/Users/USER/Desktop/convenience/blueStorage.txt", "w")
                f.write(a)
                f.close()
                f = open("C:/Users/USER/Desktop/convenience/blueStorage.txt", "r")
                s = f.readline()
                print("讀取文檔後Address:"), s
                f.close()

                # os.system('sudo hcitool cc %s' %s)
                child = pexpect.spawn('bluetoothctl')
                child.expect('\# ')
                time.sleep(1)
                child.sendline('pair %s' % s)
                time.sleep(5)
                child.sendline('yes')
                child.expect('\# ')
                child.sendline('quit')
                print('---- bluetoothctl down! ----')
                print("*****************************************************")
                var2.set("配對成功")
            except:
                var2.set("配對失敗")

        def btn11(*args):
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            btn1.config(image=photo059)

        def btn111(*args):
            btn1.config(state='disabled')
            btn1.config(image=photo028)
            scanner()

        def btn22(*args):
            btn1.config(state='disabled')
            btn3.config(state='disabled')
            btn2.config(image=photo060)

        def btn222(*args):
            btn2.config(state='disabled')
            btn2.config(image=photo029)
            choice()
            btn1.config(state='normal')
            btn2.config(state='normal')
            btn3.config(state='normal')

        def btn33(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(image=photo042)

        def btn333(*args):
            btn3.config(state='disabled')
            btn3.config(image=photo006)
            controller.switch_frame(OneofThree)

        def btn444(*args):
            self.btn44.config(image=photo057)

        def btn4444(*args):
            self.btn44.config(image=photo026)
            btn1.config(state='normal')
            btn2.config(state='normal')
            btn3.config(state='normal')
            self.btn44.place_forget()
            self.label5.place_forget()

        var1 = tk.StringVar()
        lb = tk.Listbox(self, width=36, height=6, bg='white',
                        listvariable=var1, font="Arial 28")
        lb.place(x=15, y=100)

        var2 = tk.StringVar()
        label1 = tk.Label(self, bg='gray', textvariable=var2,
                          width=35, height=1, font="Arial 28")
        label1.place(x=10, y=380)

        label3 = tk.Label(self, text='Bluetooth', font="Arial 28")
        label3.place(x=310, y=25)
        label4 = tk.Label(self, text='Device', font="Arial 28")
        label4.place(x=10, y=48)  # EN

        btn1 = tk.Button(self, image=photo028, highlightthickness=0, bd=0)
        btn2 = tk.Button(self, image=photo029, highlightthickness=0, bd=0)
        btn3 = tk.Button(self, image=photo006, highlightthickness=0, bd=0)

        btn1.place(x=110, y=450)  # ------尋找
        btn2.place(x=310, y=450)  # ------配對
        btn3.place(x=510, y=450)  # ------返回

        btn1.bind('<Button-1>', btn11)
        btn1.bind("<ButtonRelease-1>", btn111)
        btn2.bind('<Button-1>', btn22)
        btn2.bind("<ButtonRelease-1>", btn222)
        btn3.bind('<Button-1>', btn33)
        btn3.bind("<ButtonRelease-1>", btn333)

        year1, month1, date1, hour1, minute1 = read_time()
        self.label12 = tk.Label(self, text=year1, font=1)
        self.label12.place(x=10, y=5)
        self.label13 = tk.Label(self, text=month1, font=1)
        self.label13.place(x=60, y=5)
        self.label14 = tk.Label(self, text=date1, font=1)
        self.label14.place(x=88, y=5)
        self.label15 = tk.Label(self, text=hour1, font=1)
        self.label15.place(x=138, y=5)
        self.label16 = tk.Label(self, text=minute1, font=1)
        self.label16.place(x=165, y=5)
        self.update()

    def update(self):
        year1, month1, date1, hour1, minute1 = read_time()
        self.label12.config(text=year1 + '-')
        self.label13.config(text=month1 + '-')
        self.label14.config(text=date1)
        self.label15.config(text=hour1 + ':')
        self.label16.config(text=minute1)
        self.after(1000, self.update)


class Settime(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)

        def setpage():
            year1 = '0'
            month1 = '0'
            date1 = '0'
            hour1 = '0'
            minute1 = '0'
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            btn4.config(state='disabled')
            btn5.config(state='disabled')
            btn6.config(state='disabled')
            btn7.config(state='disabled')
            btn8.config(state='disabled')
            controller.switch_frame(Setting)

        def startpage():
            controller.switch_frame(StartPage)

        def keyboardshow4():
            global inputtxt
            inputtxt = 4
            controller.switch_frame(keyboard)

        def keyboardshow5():
            global inputtxt
            inputtxt = 5
            controller.switch_frame(keyboard)

        def keyboardshow6():
            global inputtxt
            inputtxt = 6
            controller.switch_frame(keyboard)

        def keyboardshow7():
            global inputtxt
            inputtxt = 7
            controller.switch_frame(keyboard)

        def keyboardshow8():
            global inputtxt
            inputtxt = 8
            controller.switch_frame(keyboard)

        def writetime():
            timeset = month11+date11+hour11+minute11+year11
            print('timeset: '+timeset)
            os.system('sudo date ' + timeset)

        def writertc():
            os.system('sudo hwclock -w')

        def save():
            self.label5 = tk.Label(self, image=photos183)
            self.label5.place(x=100, y=150)  # ------彈窗
            self.btn4 = tk.Button(self, image=photo026)
            self.btn4.place(x=315, y=300)
            self.btn4.bind('<Button-1>', btn441)
            self.btn4.bind("<ButtonRelease-1>", btn4441)

        def btn441(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            btn4.config(state='disabled')
            btn5.config(state='disabled')
            btn6.config(state='disabled')
            btn7.config(state='disabled')
            btn8.config(state='disabled')
            self.btn4.config(image=photo057)

        def btn4441(*args):
            runtimeset = threading.Thread(name='Writetime', target=writetime)
            runtimeset.start()
            while runtimeset.is_alive():
                time.sleep(0.1)
            runrtcset = threading.Thread(name='Writertc', target=writertc)
            runrtcset.start()
            while runrtcset.is_alive():
                time.sleep(0.1)
            # ---------------------------------確認後儲存
            self.btn4.config(image=photo026)
            time.sleep(1)
            os.system('sudo reboot')

        def btn11(*args):
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            btn4.config(state='disabled')
            btn5.config(state='disabled')
            btn6.config(state='disabled')
            btn7.config(state='disabled')
            btn8.config(state='disabled')
            btn1.config(image=photo061)  # -------------------輸入年份

        def btn111(*args):
            btn1.config(image=photo030)
            keyboardshow4()

        def btn22(*args):
            btn1.config(state='disabled')
            btn3.config(state='disabled')
            btn4.config(state='disabled')
            btn5.config(state='disabled')
            btn6.config(state='disabled')
            btn7.config(state='disabled')
            btn8.config(state='disabled')
            btn2.config(image=photo062)  # -------------------輸入月份

        def btn222(*args):
            btn2.config(image=photo031)
            keyboardshow5()

        def btn33(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn4.config(state='disabled')
            btn5.config(state='disabled')
            btn6.config(state='disabled')
            btn7.config(state='disabled')
            btn8.config(state='disabled')
            btn3.config(image=photo063)  # -------------------輸入日期

        def btn333(*args):
            btn3.config(image=photo032)
            keyboardshow6()

        def btn44(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            btn5.config(state='disabled')
            btn6.config(state='disabled')
            btn7.config(state='disabled')
            btn8.config(state='disabled')
            btn4.config(image=photo064)  # -------------------輸入小時

        def btn444(*args):
            btn4.config(image=photo033)
            keyboardshow7()

        def btn55(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            btn4.config(state='disabled')
            btn6.config(state='disabled')
            btn7.config(state='disabled')
            btn8.config(state='disabled')
            btn5.config(image=photo065)  # -------------------輸入分鐘

        def btn555(*args):
            btn5.config(image=photo034)
            keyboardshow8()

        def btn66(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            btn4.config(state='disabled')
            btn5.config(state='disabled')
            btn7.config(state='disabled')
            btn8.config(state='disabled')
            btn6.config(image=photo046)  # -------------------儲存

        def btn666(*args):
            btn6.config(state='disabled')
            btn6.config(image=photo010)
            save()

        def btn77(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            btn4.config(state='disabled')
            btn5.config(state='disabled')
            btn6.config(state='disabled')
            btn8.config(state='disabled')
            btn7.config(image=photo041)  # -------------------首頁

        def btn777(*args):
            btn7.config(image=photo005)
            controller.switch_frame(StartPage)

        def btn88(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            btn4.config(state='disabled')
            btn5.config(state='disabled')
            btn6.config(state='disabled')
            btn7.config(state='disabled')
            btn8.config(image=photo042)  # -------------------返回

        def btn888(*args):
            btn8.config(image=photo006)
            self.destroy()
            controller.switch_frame(Setting)

        def destroy(self):
            self.page.destroy()

        year11, month11, date11, hour11, minute11 = read_time1()

        btn1 = tk.Button(self, image=photo030,
                         highlightthickness=0, bd=0, command=keyboardshow4)
        btn2 = tk.Button(self, image=photo031,
                         highlightthickness=0, bd=0, command=keyboardshow5)
        btn3 = tk.Button(self, image=photo032,
                         highlightthickness=0, bd=0, command=keyboardshow6)
        btn4 = tk.Button(self, image=photo033,
                         highlightthickness=0, bd=0, command=keyboardshow7)
        btn5 = tk.Button(self, image=photo034,
                         highlightthickness=0, bd=0, command=keyboardshow8)

        btn1.place(x=30, y=70)  # ----------------輸入年份
        btn2.place(x=30, y=150)  # ----------------輸入月份
        btn3.place(x=30, y=230)  # ----------------輸入日期
        btn4.place(x=30, y=310)  # ----------------輸入小時
        btn5.place(x=30, y=390)  # ----------------輸入分鐘

        self.label1 = tk.Label(self, text=year11, font="Arial 28")
        self.label2 = tk.Label(self, text=month11, font="Arial 28")
        self.label3 = tk.Label(self, text=date11, font="Arial 28")
        self.label4 = tk.Label(self, text=hour11, font="Arial 28")
        self.label5 = tk.Label(self, text=minute11, font="Arial 28")
        # label16 = tk.Label(self,text='時間設置', font="Courier 24")

        self.label1.place(x=220, y=80)  # ----------------輸入年份
        self.label2.place(x=220, y=160)  # ----------------輸入月份
        self.label3.place(x=220, y=240)  # ----------------輸入日期
        self.label4.place(x=220, y=320)  # ----------------輸入小時
        self.label5.place(x=220, y=400)  # ----------------輸入分鐘
        # label16.place(x=330,y=32)                                               #----------------時間設置

        btn1.bind('<Button-1>', btn11)
        btn1.bind("<ButtonRelease-1>", btn111)  # ----------------輸入年份
        btn2.bind('<Button-1>', btn22)
        btn2.bind("<ButtonRelease-1>", btn222)  # ----------------輸入月份
        btn3.bind('<Button-1>', btn33)
        btn3.bind("<ButtonRelease-1>", btn333)  # ----------------輸入日期
        btn4.bind('<Button-1>', btn44)
        btn4.bind("<ButtonRelease-1>", btn444)  # ----------------輸入小時
        btn5.bind('<Button-1>', btn55)
        btn5.bind("<ButtonRelease-1>", btn555)  # ----------------輸入分鐘

        btn6 = tk.Button(self, image=photo010,
                         highlightthickness=0, bd=0, command=save)
        btn7 = tk.Button(self, image=photo005,
                         highlightthickness=0, bd=0, command=startpage)
        btn8 = tk.Button(self, image=photo006,
                         highlightthickness=0, bd=0, command=setpage)

        btn6.place(x=550, y=200)  # --------儲存
        # btn7.place(x=665,y=305)         #--------首頁
        btn8.place(x=550, y=350)  # --------返回

        btn6.bind('<Button-1>', btn66)
        btn6.bind("<ButtonRelease-1>", btn666)  # ----------------儲存
        btn7.bind('<Button-1>', btn77)
        btn7.bind("<ButtonRelease-1>", btn777)  # ----------------首頁
        btn8.bind('<Button-1>', btn88)
        btn8.bind("<ButtonRelease-1>", btn888)  # ----------------返回

        # self.label6 = tk.Label(self,image=photo14)
        # self.label6.place(x=230,y=1)

        # label111 = tk.Label(self,text='時間設置', font="Arial 18")
        # label111.place(x=130,y=25)

        year1, month1, date1, hour1, minute1 = read_time()
        self.label12 = tk.Label(self, text=year1, font=1)
        self.label12.place(x=10, y=5)
        self.label13 = tk.Label(self, text=month1, font=1)
        self.label13.place(x=60, y=5)
        self.label14 = tk.Label(self, text=date1, font=1)
        self.label14.place(x=88, y=5)
        self.label15 = tk.Label(self, text=hour1, font=1)
        self.label15.place(x=138, y=5)
        self.label16 = tk.Label(self, text=minute1, font=1)
        self.label16.place(x=165, y=5)
        self.update()

    def update(self):
        year1, month1, date1, hour1, minute1 = read_time()
        self.label12.config(text=year1 + '-')
        self.label13.config(text=month1 + '-')
        self.label14.config(text=date1)
        self.label15.config(text=hour1 + ':')
        self.label16.config(text=minute1)
        self.after(1000, self.update)


class keyboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, controller)

        lower_list = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']
        ]

        upper_list = [
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['G', 'H', 'I'],
            ['J', 'K', 'L'],
            ['M', 'N', 'O'],
            ['P', 'Q', 'R', 'S'],
            ['T', 'U', 'V'],
            ['W', 'X', 'Y', 'Z']
        ]

        number_list = [['1'], ['2'], ['3'], ['4'],
                       ['5'], ['6'], ['7'], ['8'], ['9']]

        global isuppercase
        isuppercase = 2
        case_list = number_list

        def startpage():
            controller.switch_frame(StartPage)

        def count_gen(n):
            def count():
                global count_list, count_list_en, values, value_current, isuppercase, last_command
                if (isuppercase == 0):
                    my_list = lower_list
                    print('0000000')
                elif (isuppercase == 1):
                    my_list = upper_list
                    print('1111111')
                elif (isuppercase == 2):
                    my_list = number_list
                    i = count_list[n] % len(my_list[n])
                    value_current = my_list[n][i]
                    entry.insert(tk.END, value_current)
                    print('2222222')
                if (isuppercase == 0 or isuppercase == 1):
                    # i = count_list_en[n] = (count_list_en[n] + 1) % len( my_list[n] )
                    # value_current = my_list [n][i-1]
                    # values.set(  str( my_list [n][i-1]) )
                    if n == last_command:
                        i = count_list_en[n] = (
                            count_list_en[n] + 1) % len(my_list[n])
                        value_current = my_list[n][i]
                        values.set(values.get()[:-1] + str(my_list[n][i]))
                    else:
                        count_list_en[last_command] = 0
                        values.set(values.get() + str(my_list[n][0]))
                        last_command = n

            return count

        def en_set():  # *
            global last_command
            last_command = -1

        def count0():
            global value_current
            value_current = 0
            entry.insert(tk.END, value_current)

        def countX():
            global value_current
            value_current = 'X'
            entry.insert(tk.END, value_current)

        def ok():
            entry.insert(tk.END, value_current)

        def clearTxt():
            pos2 = len(entry.get()) - len(entry.get())
            entry.delete(pos2, tk.END)

        def delete():
            pos2 = len(entry.get()) - 1
            entry.delete(pos2, tk.END)

        def Space():
            entry.insert(tk.END, ' ')

        def shift():
            global isuppercase, last_command
            last_command = -1
            isuppercase = isuppercase+1
            isuppercase = isuppercase % 2
            if (isuppercase == 0):
                case_list = lower_list
                here_list = lower_list
            elif (isuppercase == 1):
                case_list = upper_list
                here_list = upper_list

            if (isuppercase == 0):
                img = [photos16, photos17, photos18, photos19,
                       photos20, photos21, photos22, photos23]
                for i in range(8):
                    text_vars.append(tk.StringVar(self))
                    text_vars[i].set(' '.join(here_list[i]))
                    btn1 = tk.Button(self, image=img[i], command=count_gen(i))
                    btn1.grid(row=position[i][0],
                              column=position[i][1], pady=3)
            elif (isuppercase == 1):
                img = [photos28, photos29, photos30, photos31,
                       photos32, photos33, photos34, photos35]
                for i in range(8):
                    text_vars.append(tk.StringVar(self))
                    text_vars[i].set(' '.join(here_list[i]))
                    btn1 = tk.Button(self, image=img[i], command=count_gen(i))
                    btn1.grid(row=position[i][0],
                              column=position[i][1], pady=3)

            del here_list

            # for inx,the_var in enumerate(text_vars):
            #    the_var.set( ' '.join(case_list[inx]) )

        def number():
            global last_command, isuppercase
            isuppercase = 2
            last_command = -1
            self.btn8.grid_forget()
            self.btn5.grid_forget()
            self.btn2.grid_forget()
            self.btn_space.grid_forget()
            # btn5.config(state='disabled')
            # btn2.config(state='disabled')
            self.btn3 = tk.Button(self, image=photos10, command=count0)
            self.btn3.grid(row=4, column=1, columnspan=2)
            # self.btn3.place(x=8, y=256)  # ------切換後的0
            self.btn9 = tk.Button(self, image=photos13, command=Eng)
            self.btn9.grid(row=4, column=4)
            # self.btn5 = tk.Button(self,text='X',height=2,width=6,command=countX)
            # self.btn5.grid(row=4,column=2)
            # self.btn7 = tk.Button(self,text='清除',height=1,width=3,font="Courier 20",command=clearTxt)
            # self.btn7.place(x=166,y=338)
            # btn4.place(x=243,y=209)
            # btn6.place(x=243,y=256)
            here_list = number_list
            if (isuppercase == 2):
                img = [photos1, photos2, photos3, photos4,
                       photos5, photos6, photos7, photos8, photos9]
                for i in range(9):
                    text_vars.append(tk.StringVar(self))
                    text_vars[i].set(' '.join(here_list[i]))
                    btn1 = tk.Button(self, image=img[i], command=count_gen(i))
                    btn1.grid(row=position[i][0],
                              column=position[i][1], pady=3)
            del here_list
            case_list = number_list

            # for inx,the_var in enumerate(text_vars):
            #    the_var.set( ' '.join(case_list[inx]) )

        def Eng():
            global isuppercase
            isuppercase = 0
            self.btn3.grid_forget()
            self.btn9.grid_forget()
            # self.btn5.grid_forget()
            # self.btn7.place_forget()
            # btn5.config(state='normal')
            # btn2.config(state='normal')
            self.btn8 = tk.Button(self, image=photos25, command=number)
            # self.btn8.place(x=251,y=343)
            self.btn8.grid(row=4, column=4)
            # self.label1 = tk.Label(self,textvariable=values,font="Courier 20")
            # self.label1.grid(row=4, column=2)
            self.btn5 = tk.Button(self, image=photos24, command=shift)
            self.btn5.grid(row=4, column=1)
            self.btn2 = tk.Button(self, image=photos26, command=en_set)
            self.btn2.grid(row=3, column=3)
            self.btn_space = tk.Button(self, image=photos27, command=Space)
            self.btn_space.grid(row=4, column=2)
            # btn4.place(x=251,y=209)
            # btn4.place(x=215,y=207)
            # btn6.place(x=251,y=256)
            # btn6.place(x=219,y=252)
            here_list = lower_list
            if (isuppercase == 0):
                img = [photos16, photos17, photos18, photos19,
                       photos20, photos21, photos22, photos23]
                for i in range(8):
                    text_vars.append(tk.StringVar(self))
                    text_vars[i].set(' '.join(here_list[i]))
                    btn1 = tk.Button(self, image=img[i], command=count_gen(i))
                    btn1.grid(row=position[i][0],
                              column=position[i][1], pady=3)
            del here_list
            case_list = lower_list

            # for inx,the_var in enumerate(text_vars):
            #        the_var.set( ' '.join(case_list[inx]) )

        def printprocess1():
            self.btn3.config(state='normal')
            btn4.config(state='normal')
            # self.btn5.config(state='normal')
            btn6.config(state='normal')
            self.btn7.config(state='normal')
            self.btn9.config(state='normal')
            btn11.config(state='normal')
            btn12.config(state='normal')
            btn13.config(state='normal')
            self.btn44.place_forget()
            self.label5.place_forget()

        def inputerror():
            self.btn3.config(state='disabled')
            btn4.config(state='disabled')
            btn6.config(state='disabled')
            self.btn7.config(state='disabled')
            self.btn9.config(state='disabled')
            btn11.config(state='disabled')
            btn12.config(state='disabled')
            btn13.config(state='disabled')
            self.label5 = tk.Label(self, image=photos184)   # ----鍵盤錯誤
            self.label5.place(x=2, y=85)  # ------彈窗
            # self.label33.place(x=120,y=206)
            self.btn44 = tk.Button(self, image=photo026,
                                   command=printprocess1)   # ----確認2
            self.btn44.place(x=82, y=142)
            # self.btn44.place(x=110,y=254)
            self.btn44.bind('<Button-1>', btn444)
            self.btn44.bind("<ButtonRelease-1>", btn4444)

        def btn444(*args):
            self.btn44.config(image=photo057)    # ----確認2(反白)

        def btn4444(*args):
            self.btn44.config(image=photo026)    # ----確認2
            self.btn44.place_forget()
            self.label5.place_forget()

        def Enter():
            global show_number
            if (inputtxt == 1):
                pid = entry.get()
                p_ID = open(
                    "C:/Users/USER/Desktop/convenience/Firstep/PatientID.txt", "w")
                p_ID.write(pid)
                p_ID.close()
                controller.switch_frame(Test)
            elif (inputtxt == 2):
                oid = entry.get()
                o_ID = open(
                    "C:/Users/USER/Desktop/convenience/Firstep/OperatorID.txt", "w")
                o_ID.write(oid)
                o_ID.close()
                controller.switch_frame(Test)
            elif (inputtxt == 3):
                global searchid
                searchid = entry.get()

            elif (inputtxt == 4):  # year11
                global year
                yearin = entry.get()
                if len(yearin) > 0:
                    a = yearin.isdigit()
                    if a == True:
                        if 1 <= int(yearin):
                            year = int(yearin)
                            controller.switch_frame(Settime)
                        else:
                            inputerror()
                    else:
                        inputerror()
                else:
                    inputerror()
            elif (inputtxt == 5):
                global month
                monthin = entry.get()
                if len(monthin) > 0:
                    a = monthin.isdigit()
                    if a == True:
                        if 1 <= int(monthin) <= 12:
                            month = int(monthin)
                            controller.switch_frame(Settime)
                        else:
                            inputerror()
                    else:
                        inputerror()
                else:
                    inputerror()
            elif (inputtxt == 6):
                global date
                datein = entry.get()
                if len(datein) > 0:
                    a = datein.isdigit()
                    if a == True:
                        if 1 <= int(datein) <= 31:
                            date = int(datein)
                            controller.switch_frame(Settime)
                        else:
                            inputerror()
                    else:
                        inputerror()
                else:
                    inputerror()
            elif (inputtxt == 7):
                global hour
                hourin = entry.get()
                if len(hourin) > 0:
                    a = hourin.isdigit()
                    if a == True:
                        if 0 < int(hourin) <= 23:
                            hour = int(hourin)
                            controller.switch_frame(Settime)
                        elif str(hourin) == '0' or str(hourin) == '00':
                            hour = '00'
                            controller.switch_frame(Settime)
                        else:
                            inputerror()
                    else:
                        inputerror()
                else:
                    inputerror()
            elif (inputtxt == 8):
                global minute
                minutein = entry.get()
                if len(minutein) > 0:
                    a = minutein.isdigit()
                    if a == True:
                        if 0 < int(minutein) <= 59:
                            minute = int(minutein)
                            controller.switch_frame(Settime)
                        elif str(minutein) == '0' or str(minutein) == '00':
                            minute = '00'
                            controller.switch_frame(Settime)
                        else:
                            inputerror()
                    else:
                        inputerror()
                else:
                    inputerror()
            elif (inputtxt == 9):
                global searchdate
                searchdate = entry.get()

        values.set('')
        entry = tk.Entry(self, textvariable=values, font='Courier 40')
        entry.place(x=20, y=10, width =500, height=80)  # ------輸入框

        label111 = tk.Label(self)
        label111.grid(row=0, padx=2, pady=32)  # ------數字鍵位置移動

        position = [
            [1, 1],
            [1, 2],
            [1, 3],
            [2, 1],
            [2, 2],
            [2, 3],
            [3, 1],
            [3, 2],
            [3, 3]
        ]

        if (isuppercase == 0):
            here_list = lower_list
        elif (isuppercase == 1):
            here_list = upper_list
        elif (isuppercase == 2):
            here_list = number_list

        text_vars = []

        if (isuppercase == 0):
            img = [photos16, photos17, photos18, photos19,
                   photos20, photos21, photos22, photos23]
            for i in range(8):
                text_vars.append(tk.StringVar(self))
                text_vars[i].set(' '.join(here_list[i]))
                btn1 = tk.Button(self, image=img[i], command=count_gen(i))
                # if i == 6:
                #        i=i+1
                btn1.grid(row=position[i][0], column=position[i][1], pady=3)
        elif (isuppercase == 1):
            img = [photos28, photos29, photos30, photos31,
                   photos32, photos33, photos34, photos35]
            for i in range(8):
                text_vars.append(tk.StringVar(self))
                text_vars[i].set(' '.join(here_list[i]))
                btn1 = tk.Button(self, image=img[i], command=count_gen(i))
                btn1.grid(row=position[i][0], column=position[i][1], pady=3)
        elif (isuppercase == 2):
            img = [photos1, photos2, photos3, photos4,
                   photos5, photos6, photos7, photos8, photos9]
            for i in range(9):
                text_vars.append(tk.StringVar(self))
                text_vars[i].set(' '.join(here_list[i]))
                btn1 = tk.Button(self, image=img[i], command=count_gen(i))
                btn1.grid(row=position[i][0], column=position[i][1], pady=3)

        del here_list

        # btn4 = tk.Button(self,text='<-',height=3,width=6,command=delete)
        # btn4.place(x=242,y=96)
        # btn4.grid(row=1,column=4)

        # self.btn3 = tk.Button(self,text='0',height=3,width=6,command=count0)
        # self.btn3.grid(row=4,column=2)

        # self.label2 = tk.Label(self,text='Input Text :')
        # self.label2.grid(row=5, column=1)

        # btn6 = tk.Button(self,text='确定',height=8,width=6,command=Enter)
        # btn6.place(x=228,y=153)
        # btn6.place(x=216,y=144)
        # btn6.place(x=221,y=145)

        self.btn3 = tk.Button(self, image=photos10, command=count0)
        # self.btn3.grid(row=4,column=1)
        # self.btn3.place(x=8, y=256)  # ------0
        self.btn3.grid(row=4, column=1, columnspan=2)
        btn4 = tk.Button(self, image=photos14, command=delete)
        btn4.grid(row=1, column=4)  # ------刪除
        # self.btn5 = tk.Button(self,image=photos11,command=countX)
        # self.btn5.grid(row=4,column=2)
        btn6 = tk.Button(self, image=photos15, command=Enter)
        # btn6.place(x=236, y=142)  # ------確認
        btn6.grid(row=2, column=4, rowspan=2)
        # btn6.place(x=212,y=260)
        self.btn7 = tk.Button(self, image=photos12, command=clearTxt)
        self.btn7.grid(row=4, column=3)  # ------清除

        self.btn9 = tk.Button(self, image=photos13, command=Eng)
        self.btn9.grid(row=4, column=4)  # ------EN切換

        # label3 = tk.Label(self,image=photo14)
        # label3.place(x=230,y=1)

        """if (inputtxt==4):
                        input_text='年份'
                elif (inputtxt==5):
                        input_text='月份'
                elif (inputtxt==6):
                        input_text='日期'
                elif (inputtxt==7):
                        input_text='小時'
                elif (inputtxt==8):
                        input_text='分鐘'
                if (inputtxt==4 or inputtxt==5 or inputtxt==6 or inputtxt==7 or inputtxt==8):
                        label4 = tk.Label(
                            self,text=input_text,font="Courier 20")
                        label4.place(x=135,y=50)"""

        def btn111(*args):
            btn12.config(state='disabled')
            btn13.config(state='disabled')
            btn11.config(image=photo048)   # -----校正(反白)

        def btn1111(*args):
            btn11.config(state='disabled')
            btn11.config(image=photo012)
        #   controller.show_frame(Calibrate)  # ------校正

        def btn112(*args):
            btn11.config(image=photo047)  # ----確認(反白)

        def btn1112(*args):
            btn11.config(image=photo011)  # ----確認
            Enter()

        def btn22(*args):
            btn12.config(image=photo041)    # ----首頁(反白)

        def btn222(*args):
            btn12.config(image=photo005)
            controller.switch_frame(StartPage)  # ------首頁

        def btn33(*args):
            btn13.config(image=photo042)     # -----返回(反白)

        def btn333(*args):
            btn13.config(image=photo006)
            controller.switch_frame(StartPage)  # ------返回

        if (inputtxt == 1):
            btn11 = tk.Button(self, image=photo012,    # -----測試
                              highlightthickness=0, bd=0)  # command=cal
            # btn11.place(x=14,y=418)
            btn11.bind('<Button-1>', btn111)
            btn11.bind("<ButtonRelease-1>", btn1111)
        elif (inputtxt == 4 or inputtxt == 5 or inputtxt == 6 or inputtxt == 7 or inputtxt == 8):
            btn11 = tk.Button(self, image=photo011,
                              highlightthickness=0, bd=0, command=Enter)    # ----確認
            # btn11.place(x=14,y=418)
            btn11.bind('<Button-1>', btn112)
            btn11.bind("<ButtonRelease-1>", btn1112)  # ------左下確認

        btn12 = tk.Button(self, image=photo005,
                          highlightthickness=0, bd=0, command=startpage)   # ----首頁
        btn13 = tk.Button(self, image=photo006,
                          highlightthickness=0, bd=0)  # command=Back)       # ----返回
        btn12.bind('<Button-1>', btn22)
        btn12.bind("<ButtonRelease-1>", btn222)
        btn13.bind('<Button-1>', btn33)
        btn13.bind("<ButtonRelease-1>", btn333)

        btn12.place(x=550, y=200)  # ------首頁
        btn13.place(x=550, y=350)  # ------返回
        # btn13.place(x=210,y=190)          這一段不確定有沒有顯示出來


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

