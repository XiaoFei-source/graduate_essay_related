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
import RPi.GPIO as GPIO
import xlwt
import xlrd
import codecs
import bluetooth
import serial
import math
import pexpect
from Arduino import Arduino
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


img001 = '/home/pi/python/intech_pic(CH)/logo.png'
photo001 = ImageTk.PhotoImage(Image.open(img001))
img002 = '/home/pi/python/intech_pic(CH)/file.png'
photo002 = ImageTk.PhotoImage(Image.open(img002))
img003 = '/home/pi/python/intech_pic(CH)/test.png'
photo003 = ImageTk.PhotoImage(Image.open(img003))
img004 = '/home/pi/python/intech_pic(CH)/setup.png'
photo004 = ImageTk.PhotoImage(Image.open(img004))
img005 = '/home/pi/python/intech_pic(CH)/home.png'
photo005 = ImageTk.PhotoImage(Image.open(img005))
img006 = '/home/pi/python/intech_pic(CH)/back.png'
photo006 = ImageTk.PhotoImage(Image.open(img006))
img007 = '/home/pi/python/intech_pic(CH)/settime.png'
photo007 = ImageTk.PhotoImage(Image.open(img007))
img008 = '/home/pi/python/intech_pic(CH)/setposition.png'
photo008 = ImageTk.PhotoImage(Image.open(img008))
img009 = '/home/pi/python/intech_pic(CH)/update.png'
photo009 = ImageTk.PhotoImage(Image.open(img009))
img010 = '/home/pi/python/intech_pic(CH)/save.png'
photo010 = ImageTk.PhotoImage(Image.open(img010))
img011 = '/home/pi/python/intech_pic(CH)/confirm.png'
photo011 = ImageTk.PhotoImage(Image.open(img011))
img012 = '/home/pi/python/intech_pic(CH)/calibration.png'
photo012 = ImageTk.PhotoImage(Image.open(img012))
img013 = '/home/pi/python/intech_pic(CH)/startdetect.png'
photo013 = ImageTk.PhotoImage(Image.open(img013))

img015 = '/home/pi/python/intech_pic(CH)/print.png'
photo015 = ImageTk.PhotoImage(Image.open(img015))
img016 = '/home/pi/python/intech_pic(CH)/left.png'
photo016 = ImageTk.PhotoImage(Image.open(img016))
img017 = '/home/pi/python/intech_pic(CH)/right.png'
photo017 = ImageTk.PhotoImage(Image.open(img017))

img019 = '/home/pi/python/intech_pic(CH)/export.png'
photo019 = ImageTk.PhotoImage(Image.open(img019))

img024 = '/home/pi/python/intech_pic(CH)/lastpage.png'
photo024 = ImageTk.PhotoImage(Image.open(img024))
img025 = '/home/pi/python/intech_pic(CH)/nextpage.png'
photo025 = ImageTk.PhotoImage(Image.open(img025))
img026 = '/home/pi/python/intech_pic(CH)/confirm2.png'
photo026 = ImageTk.PhotoImage(Image.open(img026))
img027 = '/home/pi/python/intech_pic(CH)/bluetooth.png'
photo027 = ImageTk.PhotoImage(Image.open(img027))
img028 = '/home/pi/python/intech_pic(CH)/search.png'
photo028 = ImageTk.PhotoImage(Image.open(img028))
img029 = '/home/pi/python/intech_pic(CH)/pair.png'
photo029 = ImageTk.PhotoImage(Image.open(img029))
img030 = '/home/pi/python/intech_pic(CH)/enterY.png'
photo030 = ImageTk.PhotoImage(Image.open(img030))
img031 = '/home/pi/python/intech_pic(CH)/enterMon.png'
photo031 = ImageTk.PhotoImage(Image.open(img031))
img032 = '/home/pi/python/intech_pic(CH)/enterD.png'
photo032 = ImageTk.PhotoImage(Image.open(img032))
img033 = '/home/pi/python/intech_pic(CH)/enterH.png'
photo033 = ImageTk.PhotoImage(Image.open(img033))
img034 = '/home/pi/python/intech_pic(CH)/enterMin.png'
photo034 = ImageTk.PhotoImage(Image.open(img034))
img035 = '/home/pi/python/intech_pic(CH)/ID.png'
photo035 = ImageTk.PhotoImage(Image.open(img035))


img041 = '/home/pi/python/intech_pic(CH)/home1.png'
photo041 = ImageTk.PhotoImage(Image.open(img041))
img042 = '/home/pi/python/intech_pic(CH)/back1.png'
photo042 = ImageTk.PhotoImage(Image.open(img042))
img043 = '/home/pi/python/intech_pic(CH)/settime1.png'
photo043 = ImageTk.PhotoImage(Image.open(img043))
img044 = '/home/pi/python/intech_pic(CH)/setposition1.png'
photo044 = ImageTk.PhotoImage(Image.open(img044))
img045 = '/home/pi/python/intech_pic(CH)/update1.png'
photo045 = ImageTk.PhotoImage(Image.open(img045))
img046 = '/home/pi/python/intech_pic(CH)/save1.png'
photo046 = ImageTk.PhotoImage(Image.open(img046))
img047 = '/home/pi/python/intech_pic(CH)/confirm_1.png'
photo047 = ImageTk.PhotoImage(Image.open(img047))
img048 = '/home/pi/python/intech_pic(CH)/calibration1.png'
photo048 = ImageTk.PhotoImage(Image.open(img048))
img049 = '/home/pi/python/intech_pic(CH)/startdetect1.png'
photo049 = ImageTk.PhotoImage(Image.open(img049))

img051 = '/home/pi/python/intech_pic(CH)/print1.png'
photo051 = ImageTk.PhotoImage(Image.open(img051))
img052 = '/home/pi/python/intech_pic(CH)/left1.png'
photo052 = ImageTk.PhotoImage(Image.open(img052))
img053 = '/home/pi/python/intech_pic(CH)/right1.png'
photo053 = ImageTk.PhotoImage(Image.open(img053))

img055 = '/home/pi/python/intech_pic(CH)/export1.png'
photo055 = ImageTk.PhotoImage(Image.open(img055))
img056 = '/home/pi/python/intech_pic(CH)/print1.png'
photo056 = ImageTk.PhotoImage(Image.open(img056))
img057 = '/home/pi/python/intech_pic(CH)/confirm2_1.png'
photo057 = ImageTk.PhotoImage(Image.open(img057))
img058 = '/home/pi/python/intech_pic(CH)/bluetooth1.png'
photo058 = ImageTk.PhotoImage(Image.open(img058))
img059 = '/home/pi/python/intech_pic(CH)/search1.png'
photo059 = ImageTk.PhotoImage(Image.open(img059))
img060 = '/home/pi/python/intech_pic(CH)/pair1.png'
photo060 = ImageTk.PhotoImage(Image.open(img060))
img061 = '/home/pi/python/intech_pic(CH)/enterY1.png'
photo061 = ImageTk.PhotoImage(Image.open(img061))
img062 = '/home/pi/python/intech_pic(CH)/enterMon1.png'
photo062 = ImageTk.PhotoImage(Image.open(img062))
img063 = '/home/pi/python/intech_pic(CH)/enterD1.png'
photo063 = ImageTk.PhotoImage(Image.open(img063))
img064 = '/home/pi/python/intech_pic(CH)/enterH1.png'
photo064 = ImageTk.PhotoImage(Image.open(img064))
img065 = '/home/pi/python/intech_pic(CH)/enterMin1.png'
photo065 = ImageTk.PhotoImage(Image.open(img065))
img066 = '/home/pi/python/intech_pic(CH)/ID1.png'
photo066 = ImageTk.PhotoImage(Image.open(img066))
img067 = '/home/pi/python/intech_pic(CH)/left1.png'
photo067 = ImageTk.PhotoImage(Image.open(img067))
img068 = '/home/pi/python/intech_pic(CH)/right1.png'
photo068 = ImageTk.PhotoImage(Image.open(img068))
img069 = '/home/pi/python/intech_pic(CH)/yes.png'
photo069 = ImageTk.PhotoImage(Image.open(img069))
img070 = '/home/pi/python/intech_pic(CH)/yes1.png'
photo070 = ImageTk.PhotoImage(Image.open(img070))
img071 = '/home/pi/python/intech_pic(CH)/no.png'
photo071 = ImageTk.PhotoImage(Image.open(img071))
img072 = '/home/pi/python/intech_pic(CH)/no1.png'
photo072 = ImageTk.PhotoImage(Image.open(img072))
img111 = '/home/pi/python/intech_pic(CH)/1.png'
photos1 = ImageTk.PhotoImage(Image.open(img111))
img112 = '/home/pi/python/intech_pic(CH)/2.png'
photos2 = ImageTk.PhotoImage(Image.open(img112))
img113 = '/home/pi/python/intech_pic(CH)/3.png'
photos3 = ImageTk.PhotoImage(Image.open(img113))
img114 = '/home/pi/python/intech_pic(CH)/4.png'
photos4 = ImageTk.PhotoImage(Image.open(img114))
img115 = '/home/pi/python/intech_pic(CH)/5.png'
photos5 = ImageTk.PhotoImage(Image.open(img115))
img116 = '/home/pi/python/intech_pic(CH)/6.png'
photos6 = ImageTk.PhotoImage(Image.open(img116))
img117 = '/home/pi/python/intech_pic(CH)/7.png'
photos7 = ImageTk.PhotoImage(Image.open(img117))
img118 = '/home/pi/python/intech_pic(CH)/8.png'
photos8 = ImageTk.PhotoImage(Image.open(img118))
img119 = '/home/pi/python/intech_pic(CH)/9.png'
photos9 = ImageTk.PhotoImage(Image.open(img119))
img120 = '/home/pi/python/intech_pic(CH)/0.png'
photos10 = ImageTk.PhotoImage(Image.open(img120))

img122 = '/home/pi/python/intech_pic(CH)/del.png'
photos12 = ImageTk.PhotoImage(Image.open(img122))
img123 = '/home/pi/python/intech_pic(CH)/En.png'
photos13 = ImageTk.PhotoImage(Image.open(img123))
img124 = '/home/pi/python/intech_pic(CH)/backspace.png'
photos14 = ImageTk.PhotoImage(Image.open(img124))
img125 = '/home/pi/python/intech_pic(CH)/confirm3.png'
photos15 = ImageTk.PhotoImage(Image.open(img125))
img126 = '/home/pi/python/intech_pic(CH)/abc.png'
photos16 = ImageTk.PhotoImage(Image.open(img126))
img127 = '/home/pi/python/intech_pic(CH)/def.png'
photos17 = ImageTk.PhotoImage(Image.open(img127))
img128 = '/home/pi/python/intech_pic(CH)/ghi.png'
photos18 = ImageTk.PhotoImage(Image.open(img128))
img129 = '/home/pi/python/intech_pic(CH)/jkl.png'
photos19 = ImageTk.PhotoImage(Image.open(img129))
img130 = '/home/pi/python/intech_pic(CH)/mno.png'
photos20 = ImageTk.PhotoImage(Image.open(img130))
img131 = '/home/pi/python/intech_pic(CH)/pqrs.png'
photos21 = ImageTk.PhotoImage(Image.open(img131))
img132 = '/home/pi/python/intech_pic(CH)/tuv.png'
photos22 = ImageTk.PhotoImage(Image.open(img132))
img133 = '/home/pi/python/intech_pic(CH)/wxyz.png'
photos23 = ImageTk.PhotoImage(Image.open(img133))
img134 = '/home/pi/python/intech_pic(CH)/shift.png'
photos24 = ImageTk.PhotoImage(Image.open(img134))
img135 = '/home/pi/python/intech_pic(CH)/123.png'
photos25 = ImageTk.PhotoImage(Image.open(img135))
img136 = '/home/pi/python/intech_pic(CH)/en_set.png'
photos26 = ImageTk.PhotoImage(Image.open(img136))
img137 = '/home/pi/python/intech_pic(CH)/space.png'
photos27 = ImageTk.PhotoImage(Image.open(img137))
img138 = '/home/pi/python/intech_pic(CH)/u_ABC.png'
photos28 = ImageTk.PhotoImage(Image.open(img138))
img139 = '/home/pi/python/intech_pic(CH)/u_DEF.png'
photos29 = ImageTk.PhotoImage(Image.open(img139))
img140 = '/home/pi/python/intech_pic(CH)/u_GHI.png'
photos30 = ImageTk.PhotoImage(Image.open(img140))
img141 = '/home/pi/python/intech_pic(CH)/u_JKL.png'
photos31 = ImageTk.PhotoImage(Image.open(img141))
img142 = '/home/pi/python/intech_pic(CH)/u_MNO.png'
photos32 = ImageTk.PhotoImage(Image.open(img142))
img143 = '/home/pi/python/intech_pic(CH)/u_PQRS.png'
photos33 = ImageTk.PhotoImage(Image.open(img143))
img144 = '/home/pi/python/intech_pic(CH)/u_TUV.png'
photos34 = ImageTk.PhotoImage(Image.open(img144))
img145 = '/home/pi/python/intech_pic(CH)/u_WXYZ.png'
photos35 = ImageTk.PhotoImage(Image.open(img145))

img155 = '/home/pi/python/intech_pic(CH)/clearData.png'
photos155 = ImageTk.PhotoImage(Image.open(img155))
img156 = '/home/pi/python/intech_pic(CH)/clearData1.png'
photos156 = ImageTk.PhotoImage(Image.open(img156))
img157 = '/home/pi/python/intech_pic(CH)/more.png'
photos157 = ImageTk.PhotoImage(Image.open(img157))
img158 = '/home/pi/python/intech_pic(CH)/more1.png'
photos158 = ImageTk.PhotoImage(Image.open(img158))
img159 = '/home/pi/python/intech_pic(CH)/cancel.png'
photos159 = ImageTk.PhotoImage(Image.open(img159))
img160 = '/home/pi/python/intech_pic(CH)/cancel1.png'
photos160 = ImageTk.PhotoImage(Image.open(img160))
img146 = '/home/pi/python/intech_pic(CH)/printing.png'
photos36 = ImageTk.PhotoImage(Image.open(img146))
img147 = '/home/pi/python/intech_pic(CH)/removing.png'
photos37 = ImageTk.PhotoImage(Image.open(img147))

img147_ex1 = '/home/pi/python/intech_pic(CH)/exporting1.png'
photos_ex1 = ImageTk.PhotoImage(Image.open(img147_ex1))
img147_ex2 = '/home/pi/python/intech_pic(CH)/exporting2.png'
photos_ex2 = ImageTk.PhotoImage(Image.open(img147_ex2))
img147_ex3 = '/home/pi/python/intech_pic(CH)/exporting3.png'
photos_ex3 = ImageTk.PhotoImage(Image.open(img147_ex3))

img148_cal1 = '/home/pi/python/intech_pic(CH)/caling1.png'
photos_cal1 = ImageTk.PhotoImage(Image.open(img148_cal1))
img148_cal2 = '/home/pi/python/intech_pic(CH)/caling2.png'
photos_cal2 = ImageTk.PhotoImage(Image.open(img148_cal2))
img148_cal3 = '/home/pi/python/intech_pic(CH)/caling3.png'
photos_cal3 = ImageTk.PhotoImage(Image.open(img148_cal3))

img149_test1 = '/home/pi/python/intech_pic(CH)/testing1.png'
photos_test1 = ImageTk.PhotoImage(Image.open(img149_test1))
img149_test2 = '/home/pi/python/intech_pic(CH)/testing2.png'
photos_test2 = ImageTk.PhotoImage(Image.open(img149_test2))
img149_test3 = '/home/pi/python/intech_pic(CH)/testing3.png'
photos_test3 = ImageTk.PhotoImage(Image.open(img149_test3))

img150_QR1 = '/home/pi/python/intech_pic(CH)/QRing1.png'
photos_QR1 = ImageTk.PhotoImage(Image.open(img150_QR1))
img150_QR2 = '/home/pi/python/intech_pic(CH)/QRing2.png'
photos_QR2 = ImageTk.PhotoImage(Image.open(img150_QR2))
img150_QR3 = '/home/pi/python/intech_pic(CH)/QRing3.png'
photos_QR3 = ImageTk.PhotoImage(Image.open(img150_QR3))

img151 = '/home/pi/python/intech_pic(CH)/itemnext.png'
photos151 = ImageTk.PhotoImage(Image.open(img151))
img152 = '/home/pi/python/intech_pic(CH)/itemlast.png'
photos152 = ImageTk.PhotoImage(Image.open(img152))

img161 = '/home/pi/python/intech_pic(CH)/glass.png'
photos161 = ImageTk.PhotoImage(Image.open(img161))
img162 = '/home/pi/python/intech_pic(CH)/glass2.png'
photos162 = ImageTk.PhotoImage(Image.open(img162))
img163 = '/home/pi/python/intech_pic(CH)/glass3.png'
photos163 = ImageTk.PhotoImage(Image.open(img163))
img164 = '/home/pi/python/intech_pic(CH)/glass4.png'
photos164 = ImageTk.PhotoImage(Image.open(img164))

img165 = '/home/pi/python/intech_pic(CH)/bluePrinter.png'
photos165 = ImageTk.PhotoImage(Image.open(img165))
img166 = '/home/pi/python/intech_pic(CH)/bluePrinter1.png'
photos166 = ImageTk.PhotoImage(Image.open(img166))
img167 = '/home/pi/python/intech_pic(CH)/blueStorage.png'
photos167 = ImageTk.PhotoImage(Image.open(img167))
img168 = '/home/pi/python/intech_pic(CH)/blueStorage1.png'
photos168 = ImageTk.PhotoImage(Image.open(img168))
img169 = '/home/pi/python/intech_pic(CH)/DataExport.png'
photos169 = ImageTk.PhotoImage(Image.open(img169))
img170 = '/home/pi/python/intech_pic(CH)/DataExport1.png'
photos170 = ImageTk.PhotoImage(Image.open(img170))

img171 = '/home/pi/python/intech_pic(CH)/FNF.png'
photos171 = ImageTk.PhotoImage(Image.open(img171))
img172 = '/home/pi/python/intech_pic(CH)/AUS.png'
photos172 = ImageTk.PhotoImage(Image.open(img172))

#img173 = '/home/pi/python/intech_pic(CH)/Firstep-LOGO-gray.png'
# photos173=ImageTk.PhotoImage(Image.open(img173))
l = 'DESIGN'

img174 = '/home/pi/python/intech_pic(CH)/CalWarning.png'
photos174 = ImageTk.PhotoImage(Image.open(img174))
img175 = '/home/pi/python/intech_pic(CH)/CalError.png'
photos175 = ImageTk.PhotoImage(Image.open(img175))

img176 = '/home/pi/python/intech_pic(CH)/qrerror.png'
photos176 = ImageTk.PhotoImage(Image.open(img176))

img177 = '/home/pi/python/intech_pic(CH)/Success.png'
photos177 = ImageTk.PhotoImage(Image.open(img177))
img178 = '/home/pi/python/intech_pic(CH)/OKprinter.png'
photos178 = ImageTk.PhotoImage(Image.open(img178))

img179 = '/home/pi/python/intech_pic(CH)/BluePrinter_PleaseConnect.png'
photos179 = ImageTk.PhotoImage(Image.open(img179))

img180 = '/home/pi/python/intech_pic(CH)/btupdate.png'
photos180 = ImageTk.PhotoImage(Image.open(img180))

img181 = '/home/pi/python/intech_pic(CH)/BluetoothExport_PleaseConnect.png'
photos181 = ImageTk.PhotoImage(Image.open(img181))

img182 = '/home/pi/python/intech_pic(CH)/QueryBTPrinter.png'
photos182 = ImageTk.PhotoImage(Image.open(img182))

img183 = '/home/pi/python/intech_pic(CH)/settime_change.png'
photos183 = ImageTk.PhotoImage(Image.open(img183))

img184 = '/home/pi/python/intech_pic(CH)/keyboard_error.png'
photos184 = ImageTk.PhotoImage(Image.open(img184))

img185 = '/home/pi/python/intech_pic(CH)/Success_export.png'
photos185 = ImageTk.PhotoImage(Image.open(img185))

img186 = '/home/pi/python/intech_pic(CH)/Bluetooth_Error.png'
photos186 = ImageTk.PhotoImage(Image.open(img186))


# new picture

QRcode = ImageTk.PhotoImage(Image.open(
    '/home/pi/python/intech_pic(CH)/qr_code.png'))


keyboard_show = 'matchbox-keyboard'

keyboard_show = 'matchbox-keyboard'

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

class SampleApp(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.switch_frame(Test)

    def switch_frame(self, c):
        '''Show a frame for the given class'''
        frame = c(root, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

class Test(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, height="600", width="800")

        time.sleep(0.1)
        print("LED OFF!")

        #pid = readID()
        pid = "Testing"

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
            #print('--------------------------------------------test line.--------------------------------------------')
            print('----test line1----')
            self.destroy()
            root.after(1000)
            #controller.switch_frame(ButtonOK)
            ##下面先屏蔽掉
            #setup()
            #openT(4)
            #run_t1()

        def startpage():
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            # btn3.config(state='disabled')
            # btn4.config(state='disabled')
            btn5.config(state='disabled')
            #controller.switch_frame(StartPage)
            #先把按鈕功能隱藏掉

        def btn55(*args):
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn5.config(state='disabled')
            btn5.config(image=photo042)

        def btn555(*args):
            btn5.config(image=photo006)
            #controller.switch_frame(QRscan)
            #先把按鈕功能隱藏掉

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
            #controller.switch_frame(keyboard)
            #先把按鈕功能隱藏掉

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

        #testtype = str(testtype_read())
        testtype = "1"
        #resulttype = resulttype_read()
        resulttype ="2"

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

            #return result_text_A

        # M_choose

        # 只留1C2T
        if testtype == "1":
            #A_item = T1_item_read("A")
            A_item = "MET"
            #A_item_t2 = T2_item_read("A")
            A_item_t2 = "MOR"
            print("A_item =", A_item)

            result_text_A = resulttype_check()
            # pos_show_1C2T(result_text, x, label_resulttype_pos, label_c_line_pos, label_item_pos, label_item1_pos, item, item1):
            pos_show_1C2T(result_text_A, 15, 270, 330,
                          390, 450, A_item, A_item_t2)
            # ('c', A_c_concentration, 250, A_item_T2, A_item_T1, A_t2_concentration,
            # , A_t2_result_c, A_t1_result_c, 10, 30, 300, 350)
        elif testtype == "2":
            #A_item = T1_item_read("B")
            A_item = "MET"
            #A_item_t2 = T2_item_read("B")
            A_item_t2 = "MOR"
            print("A_item =", A_item)

            result_text_A = resulttype_check()

            pos_show_1C2T(result_text_A, 15, 270, 330,
                          390, 450, A_item, A_item_t2)
            # ('c', A_c_concentration, 250, A_item_T2, A_item_T1, A_t2_concentration,
            # A_t1_concentration, A_t2_result_c, A_t1_result_c, 10, 30, 300, 350)
        elif testtype == "3":
            #A_item = T1_item_read("C")
            A_item = "MET"
            #A_item_t2 = T2_item_read("C")
            A_item_t2 = "MOR"
            print("A_item =", A_item)

            result_text_A = resulttype_check()

            pos_show_1C2T(result_text_A, 15, 270, 330,
                          390, 450, A_item, A_item_t2)
            # ('c', A_c_concentration, 250, A_item_T2, A_item_T1, A_t2_concentration,
            # , A_t2_result_c, A_t1_result_c, 10, 30, 300, 350)
        else:
            print("Error,what the hell do you mean")

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
