import os
import sys
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
#Keys được dùng cho các thao tác dùng nút trên bàn phím (Ctrl, ALT,...)
from selenium.webdriver.common.by import By
#Thuộc tính By dùng để định vị các element (Ex: By.ID, By.Name, By.XPATH,...)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Thư viện anyascii dùng để chuẩn hóa chuỗi

import pandas as pd

import smtplib
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

## The pandas library is only for generating the current date, which is not necessary for sending emails

from datetime import datetime, timedelta


window = tk.Tk()
window.geometry("300x550")
window.resizable(False, False)
login_fr = Frame(window)
login_fr.pack(pady = 10)
username_fr = Frame(login_fr)
username_fr.pack()
username_lbl = Label(username_fr, text="Username: ")
username_lbl.pack(side=LEFT)
username_value = tk.StringVar()
username_input = Entry(username_fr, textvariable=username_value)
username_input.pack(side=LEFT)

password_fr = Frame(login_fr)
password_fr.pack(pady=5)
password_lbl = Label(password_fr, text="Password:  ")
password_lbl.pack(side=LEFT)
password_value = tk.StringVar()
password_input = Entry(password_fr, textvariable = password_value, show="*")
password_input.pack(side=LEFT)

username_check_fr = Frame(login_fr)
username_check_fr.pack()
username_check_lbl = Label(username_check_fr, text="", wraplengt=200)
username_check_lbl.pack()

date_fr = Frame(login_fr)
date_fr.pack()
date_lbl = Label(date_fr, text = "Choose date:")
date_lbl.pack()
date_picker_fr = Frame(date_fr)
date_picker_fr.pack(pady=5, expand=1, fill=X)

get_date = datetime.now()

day= []
for i in range(1,32):
    day.append(str("{:02d}".format(i)))

day_fr = Frame(date_picker_fr)
day_fr.pack(side = LEFT)
day_lbl = Label(day_fr, text = "Day: ")
day_lbl.pack(side = LEFT)
selected_day=tk.StringVar()
day_cbb = ttk.Combobox(day_fr, textvariable=selected_day, width=2)
day_cbb.pack(side = LEFT)
day_cbb["value"] = day
day_cbb.set(get_date.strftime("%d"))
day_cbb["state"]="readonly"

month = []
for i in range(1, 13):
    month.append(str("{:02d}".format(i)))
month_fr = Frame(date_picker_fr)
month_fr.pack(side = LEFT)
month_lbl = Label(month_fr, text = "Month: ")
month_lbl.pack(side = LEFT)
selected_month=tk.StringVar()
month_cbb = ttk.Combobox(month_fr, textvariable=selected_month, width=2)
month_cbb.pack(side = LEFT)
month_cbb["value"] = month
month_cbb.set(get_date.strftime("%m"))
month_cbb["state"]="readonly"

year = []
for i in range(2000, 2051):
    year.append(i)
year_fr = Frame(date_picker_fr)
year_fr.pack(side = LEFT)
year_lbl = Label(year_fr, text = "Year: ")
year_lbl.pack(side = LEFT)
selected_year=tk.StringVar()
year_cbb = ttk.Combobox(year_fr, textvariable=selected_year, width=4)
year_cbb.pack(side = LEFT)
year_cbb["value"] = year
year_cbb.set(get_date.strftime("%Y"))
year_cbb["state"]="readonly"

def set_day_morning_shift():
    day_cbb.set(get_date.strftime("%d"))

def set_day_afternoon_shift():
    day_cbb.set(get_date.strftime("%d"))

def set_day_night_shift():
    get_previous_day = datetime.today() - timedelta(days=1)
    day_cbb.set(get_previous_day.strftime("%d"))


shift_fr = Frame(login_fr)
shift_fr.pack(pady=5)
shift_lbl = Label(shift_fr, text="Choose shift:")
shift_lbl.pack()
selected_shift=tk.IntVar()
shift_area_fr=Frame(shift_fr)
shift_area_fr.pack()
now = datetime.now()
hour = now.hour
minute = now.minute
morning_radiobtn=tk.Radiobutton(shift_area_fr, text="Morning", variable=selected_shift, value="1", command=set_day_morning_shift)
morning_radiobtn.pack(side=LEFT)
if timedelta(hour, minute) > timedelta(13, 0) and timedelta(hour, minute) < timedelta(15, 0):
    morning_radiobtn.select()
afternoon_radiobtn=tk.Radiobutton(shift_area_fr, text="Afternoon", variable=selected_shift, value="2", command=set_day_afternoon_shift)
afternoon_radiobtn.pack(side=LEFT)
if timedelta(hour, minute) > timedelta(21, 0) and timedelta(hour, minute) < timedelta(23, 0):
    afternoon_radiobtn.select()
night_radiobtn=tk.Radiobutton(shift_area_fr, text="Night", variable=selected_shift, value="3", command=set_day_night_shift)
night_radiobtn.pack(side=LEFT)
if timedelta(hour, minute) > timedelta(5, 0) and timedelta(hour, minute) < timedelta(7, 0):
    night_radiobtn.select()

#Kiểm tra ca đang được chọn để set ngày phù hợp khi load form 
if selected_shift.get() == 1:
    set_day_morning_shift()
elif selected_shift.get() == 2:
    set_day_afternoon_shift()
else:
    set_day_night_shift()

leader_fr=Frame(login_fr)
leader_fr.pack(fill=X, expand=1)
leader_lbl=Label(leader_fr, text="Leader")
leader_lbl.pack()
choose_leader_fr=Frame(leader_fr)
choose_leader_fr.pack(fill=X, expand=1)
leader_fr_1_parent = Frame(choose_leader_fr)
leader_fr_1_parent.pack(fill=X, expand=1)
leader_fr_1 = Frame(leader_fr_1_parent)
leader_fr_1.pack(side=LEFT, padx=80)
selected_leader_1=tk.IntVar()
leader_check_1=ttk.Checkbutton(leader_fr_1, text="JamesLee", variable=selected_leader_1, onvalue=1, offvalue=0)
leader_check_1.pack()
leader_fr_2_parent = Frame(choose_leader_fr)
leader_fr_2_parent.pack(fill=X, expand=1)
leader_fr_2 = Frame(leader_fr_2_parent)
leader_fr_2.pack(side=LEFT, padx=80)
selected_leader_2=tk.IntVar()
leader_check_2=ttk.Checkbutton(leader_fr_2, text="Trình", variable=selected_leader_2, onvalue=1, offvalue=0)
leader_check_2.pack()
leader_fr_3_parent = Frame(choose_leader_fr)
leader_fr_3_parent.pack(fill=X, expand=1)
leader_fr_3 = Frame(leader_fr_3_parent)
leader_fr_3.pack(side=LEFT, padx=80)
selected_leader_3=tk.IntVar()
leader_check_3=ttk.Checkbutton(leader_fr_3, text="Luận", variable=selected_leader_3, onvalue=1, offvalue=0)
leader_check_3.pack()
leader_fr_4_parent = Frame(choose_leader_fr)
leader_fr_4_parent.pack(fill=X, expand=1)
leader_fr_4 = Frame(leader_fr_4_parent)
leader_fr_4.pack(side=LEFT, padx=80)
selected_leader_4=tk.IntVar()
leader_check_4=ttk.Checkbutton(leader_fr_4, text="Hiếu", variable=selected_leader_4, onvalue=1, offvalue=0)
leader_check_4.pack()
leader_fr_5_parent = Frame(choose_leader_fr)
leader_fr_5_parent.pack(fill=X, expand=1)
leader_fr_5 = Frame(leader_fr_5_parent)
leader_fr_5.pack(side=LEFT, padx=80)
selected_leader_5=tk.IntVar()
leader_check_5=ttk.Checkbutton(leader_fr_5, text="Thảo", variable=selected_leader_5, onvalue=1, offvalue=0)
leader_check_5.pack()
leader_fr_6_parent = Frame(choose_leader_fr)
leader_fr_6_parent.pack(fill=X, expand=1)
leader_fr_6 = Frame(leader_fr_6_parent)
leader_fr_6.pack(side=LEFT, padx=80)
selected_leader_6=tk.IntVar()
leader_check_6=ttk.Checkbutton(leader_fr_6, text="Chay", variable=selected_leader_6, onvalue=1, offvalue=0)
leader_check_6.pack()
leader_fr_7_parent = Frame(choose_leader_fr)
leader_fr_7_parent.pack(fill=X, expand=1)
leader_fr_7 = Frame(leader_fr_7_parent)
leader_fr_7.pack(side=LEFT, padx=80)
selected_leader_7=tk.IntVar()
leader_check_7=ttk.Checkbutton(leader_fr_7, text="Nhân", variable=selected_leader_7, onvalue=1, offvalue=0)
leader_check_7.pack()
leader_fr_8_parent = Frame(choose_leader_fr)
leader_fr_8_parent.pack(fill=X, expand=1)
leader_fr_8 = Frame(leader_fr_8_parent)
leader_fr_8.pack(side=LEFT, padx=80)
selected_leader_8=tk.IntVar()
leader_check_8=ttk.Checkbutton(leader_fr_8, text="Thịnh", variable=selected_leader_8, onvalue=1, offvalue=0)
leader_check_8.pack()

mail_fr=Frame(login_fr)
mail_fr.pack(expand=1, fill=X, pady=10)
mail_lbl=Label(mail_fr, text="Email")
mail_lbl.pack()
mail_username_fr_parent = Frame(mail_fr)
mail_username_fr_parent.pack(expand=1, fill=X)
mail_username_fr=Frame(mail_username_fr_parent)
mail_username_fr.pack(side=LEFT, padx=10)
mail_username_lbl=Label(mail_username_fr, text="Email Address: ")
mail_username_lbl.pack(side=LEFT)
mail_username_value=tk.StringVar()
mail_username_input=Entry(mail_username_fr, textvariable=mail_username_value, width=15)
mail_username_input.pack(side=LEFT)
mail_tailer = Label(mail_username_fr, text="@sms-vn.com")
mail_tailer.pack(side=LEFT)

mail_password_fr_parent = Frame(mail_fr)
mail_password_fr_parent.pack(expand=1, fill=X, pady=5)
mail_password_fr=Frame(mail_password_fr_parent)
mail_password_fr.pack(side=LEFT, padx=3)
mail_password_lbl=Label(mail_password_fr, text="Email Password: ")
mail_password_lbl.pack(side=LEFT)
mail_password_value=tk.StringVar()
mail_password_input=Entry(mail_password_fr, textvariable=mail_password_value, show="*", width=15)
mail_password_input.pack(side=LEFT)


def wr_submit():
    #Sử dụng nhị phân mặc định của chrome thay vì chromedriver
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)

    #Sử dụng nhị phân mặc định của chrome thay vì chromedriver
    options = Options()
    options.binary_location = "C:\\Program Files\\Chrome\\chrome.exe"
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(executable_path=resource_path('.\\driver\\chromedriver.exe'))
    driver = webdriver.Chrome(options = options, service = service)
    driver.get("https://mis-wr.smsvn.local/wr/login.php")
    #Định vị element username, password theo ID
    username = driver.find_element(By.XPATH, value="/html/body/div[@id='login_form']/form[@class='form-signin']/p[1]/input[@class='form-control']")
    username.send_keys(username_value.get())
    password = driver.find_element(By.XPATH, value="/html/body/div[@id='login_form']/form[@class='form-signin']/p[2]/input[@class='form-control']")
    password.send_keys(password_value.get())

    #Định vị nút login theo tên bằng XPATH
    login = driver.find_element(By.XPATH, value="/html/body/div[@id='login_form']/form[@class='form-signin']/button[@class='btn btn-lg btn-primary btn-block']")
    login.click()

    working_report=driver.find_element(By.XPATH, value="/html/body/nav[@class='navbar navbar-default navbar-fixed-top']/div[@class='container-fluid']/div[@id='bs-example-navbar-collapse-1']/ul[@class='nav navbar-nav']/li[@class='dropdown'][1]/a[@class='dropdown-toggle']")
    working_report.click()
    show_report = driver.find_element(By.PARTIAL_LINK_TEXT, "Show Report")
    show_report.click()
    choose_day = driver.find_element(By.ID, "datepicker")
    choose_day.clear()
    date_chosen=selected_month.get()+"/"+selected_day.get()+"/"+selected_year.get()
    choose_day.send_keys(date_chosen)
    choose_day.send_keys(Keys.ENTER)
    if selected_shift.get() == 1:        
        choose_shift=driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/form/p[2]/input[2]")
        choose_shift.click()
    if selected_shift.get() == 2:
        choose_shift=driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/form/p[2]/input[3]")
        choose_shift.click()
    if selected_shift.get() == 3:
        choose_shift=driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/form/p[2]/input[4]")
        choose_shift.click()
    view=driver.find_element(By.XPATH, value="/html/body/div[@class='container']/div[@class='row']/div[@class='col-sm-6'][1]/form[@class='form-signin']/button[@class='btn btn-lg btn-primary btn-block']")
    view.click()
    time_sort=driver.find_element(By.XPATH, value="//*[@id='example_wrapper']/div[3]/div[1]/div/table/thead/tr[1]/th[7]/a")
    driver.execute_script("arguments[0].click();", time_sort)
    search=driver.find_element(By.XPATH, value="/html/body/form[2]/div[@class='container']/div[@id='example_wrapper']/div[@id='example_filter']/label/input")
    search.send_keys(username_value.get())
    rows = driver.find_elements(By.XPATH, value="//*[@id='example']/tbody/tr")

    tmp = []

    try:
        for i in range(len(rows)):
            # cell = driver.find_element(By.XPATH, value = "//*[@id='example']/tbody/tr["+ "{}".format(i+1) + "]")
            time = driver.find_element(By.XPATH, value = "//*[@id='example']/tbody/tr[" + "{}".format(i+1) + "]/td[12]/div")
            total_time = driver.find_element(By.XPATH, value = "//*[@id='example']/tbody/tr[" + "{}".format(i+1) + "]/td[15]/div")
            staff = driver.find_element(By.XPATH, value = "//*[@id='example']/tbody/tr[" + "{}".format(i+1) + "]/td[16]/div")
            user = driver.find_element(By.XPATH, value = "//*[@id='example']/tbody/tr[" + "{}".format(i+1) + "]/td[18]/div")
            position = driver.find_element(By.XPATH, value = "//*[@id='example']/tbody/tr[" + "{}".format(i+1) + "]/td[19]/div")
            dept = driver.find_element(By.XPATH, value = "//*[@id='example']/tbody/tr[" + "{}".format(i+1) + "]/td[20]/div")
            inventory = driver.find_element(By.XPATH, value = "//*[@id='example']/tbody/tr[" + "{}".format(i+1) + "]/td[21]/div")
            problem = driver.find_element(By.XPATH, value = "//*[@id='example']/tbody/tr[" + "{}".format(i+1) + "]/td[22]/div")
            reason = driver.find_element(By.XPATH, value = "//*[@id='example']/tbody/tr[" + "{}".format(i+1) + "]/td[23]/div")
            solution = driver.find_element(By.XPATH, value = "//*[@id='example']/tbody/tr[" + "{}".format(i+1) + "]/td[24]/div")
            replace_old = driver.find_element(By.XPATH, value = "//*[@id='example']/tbody/tr[" + "{}".format(i+1) + "]/td[26]")
            replace_new = driver.find_element(By.XPATH, value = "//*[@id='example']/tbody/tr[" + "{}".format(i+1) + "]/td[27]")
            staff_to_list = list(staff.text.split(", "))
            if username_value.get() in staff_to_list:
                tmp.extend((time.text, total_time.text, user.text, position.text, dept.text, inventory.text, problem.text, reason.text, solution.text, replace_old.text, replace_new.text))       

    except Exception:
        pass

    entry_list = []

    s = 0
    while s < len(tmp):
        tmp1 = tmp[s:s+11]
        s=s+11
        entry_list.append(tmp1)

    if selected_shift.get() == 3:
        # x = tk.IntVar()
        x = 0
        for entry in entry_list:
            entry_tmp = entry[0]
            entry_tmp1 = int(entry_tmp[0:2])
            if entry_tmp1 > 7:
                x = entry_list.index(entry)
        s1 = []
        s2 = []

        for i in range(len(entry_list)):
            if i < x:
                s1.append(entry_list[i])
            else:
                s2.append(entry_list[i])

        entry_list.clear()
        entry_list = s2 + s1
    if selected_shift.get() == 1 and len(entry_list) != 0:
        entry_list.pop(0) 

    # Define the HTML document
    html = '''
        <html>
            <body>
                <table style="border-collapse:collapse; font-size:18px;>
                <table border="01" cellspacing="0">
                    <colgroup width="121">
                    </colgroup>
                    <colgroup width="142">
                    </colgroup>
                    <colgroup width="111">
                    </colgroup>
                    <colgroup width="719">
                    </colgroup>
                    <tbody>
                            <tr>
                                <td colspan="2" style="border:1px solid black; text-align:center; vertical-align:middle; padding-top:1px; padding-right:1px; padding-left:1px; white-space:nowrap; background-color:silver;"><span style="font-size:18px"><span style="font-weight:700"><span style="color:black"><span style="font-style:normal"><span style="text-decoration:none"><span style="font-family:&quot;Liberation Sans1&quot;">TIME</span></span></span></span></span></span></td>
                                <td rowspan="2" style="border:1px solid black; text-align:center; vertical-align:middle; padding-top:1px; padding-right:1px; padding-left:1px; white-space:nowrap; background-color:silver;"><span style="font-size:18px"><span style="font-weight:700"><span style="color:black"><span style="font-style:normal"><span style="text-decoration:none"><span style="font-family:&quot;Liberation Sans1&quot;">NAME</span></span></span></span></span></span></td>
                                <td rowspan="2" style="border:1px solid black; text-align:center; vertical-align:middle; padding-top:1px; padding-right:1px; padding-left:1px; white-space:nowrap; background-color:silver;"><span style="font-size:18px"><span style="font-weight:700"><span style="color:black"><span style="font-style:normal"><span style="text-decoration:none"><span style="font-family:&quot;Liberation Sans1&quot;">DETAIL OF JOBS</span></span></span></span></span></span></td>
                                <td rowspan="2" style="border:1px solid black; text-align:center; vertical-align:middle; padding-top:1px; padding-right:1px; padding-left:1px; white-space:nowrap; background-color:silver;"><span style="font-size:18px"><span style="font-weight:700"><span style="color:black"><span style="font-style:normal"><span style="text-decoration:none"><span style="font-family:&quot;Liberation Sans1&quot;">REMARK</span></span></span></span></span></span></td>
                            </tr>
                            <tr>
                                <td style="border:1px solid black; text-align:center; padding-top:1px; padding-right:1px; padding-left:1px; vertical-align:bottom; white-space:nowrap; background-color:silver;"><span style="font-size:18px"><span style="font-weight:700"><span style="color:black"><span style="font-style:normal"><span style="text-decoration:none"><span style="font-family:&quot;Liberation Sans1&quot;">&nbsp;Start</span></span></span></span></span></span></td>
                                <td style="border:1px solid black; text-align:center; padding-top:1px; padding-right:1px; padding-left:1px; vertical-align:bottom; white-space:nowrap; background-color:silver;"><span style="font-size:18px"><span style="font-weight:700"><span style="color:black"><span style="font-style:normal"><span style="text-decoration:none"><span style="font-family:&quot;Liberation Sans1&quot;">End</span></span></span></span></span></span></td>
                            </tr>'''
    a = 0
    if len(entry_list) == 0:
        a = 1
    if selected_shift.get() == 1:
        html = html + "<tr>"
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>06:00</td>"
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>06:10</td>"                    
        html = html + "<td rowspan='"+str(len(entry_list) + a + 4)+"' style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>"+username_value.get()+"</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>Made and send Ping Plotter report, MRTG &amp; PRTG report to IT-Team</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>&nbsp;</td>"
        html = html + "</tr>"
        html = html + "<tr>"
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>06:10</td>"
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>06:20</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>Check mail and read report from previous shift</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>&nbsp;</td>"
        html = html + "</tr>" 
    if selected_shift.get() == 2:
        html = html + "<tr>"
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>14:00</td>"
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>14:10</td>"                    
        html = html + "<td rowspan='"+str(len(entry_list) + a + 3)+"' style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>"+username_value.get()+"</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>Check mail and read report from previous shift</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>&nbsp;</td>"
        html = html + "</tr>"
    if selected_shift.get() == 3:
        html = html + "<tr>"
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>22:00</td>"
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>22:10</td>"                    
        html = html + "<td rowspan='"+str(len(entry_list) + a + 3)+"' style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>"+username_value.get()+"</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>Check mail and read report from previous shift</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>&nbsp;</td>"
        html = html + "</tr>"
    if len(entry_list) == 0:
        if selected_shift.get() == 1:
            html = html + "<tr>"
            html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>07:00</td>"
            html = html + "<td style='border:1px solid black; text-align:center; vertical -align:middle; font-family:&quot;Liberation Sans1&quot;'>14:00</td>"
            html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>Stand by for supporting</td>"
            html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>&nbsp;</td>"
            html = html + "</tr>" 
        if selected_shift.get() == 2:
            html = html + "<tr>"
            html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>14:00</td>"
            html = html + "<td style='border:1px solid black; text-align:center; vertical -align:middle; font-family:&quot;Liberation Sans1&quot;'>22:00</td>"
            html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>Stand by for supporting</td>"
            html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>&nbsp;</td>"
            html = html + "</tr>" 
        if selected_shift.get() == 3:
            html = html + "<tr>"
            html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>22:00</td>"
            html = html + "<td style='border:1px solid black; text-align:center; vertical -align:middle; font-family:&quot;Liberation Sans1&quot;'>06:00</td>"
            html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>Stand by for supporting</td>"
            html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>&nbsp;</td>"
            html = html + "</tr>" 
    else:
        for entry in entry_list:
            for i in range(len(entry)):
                t = datetime.strptime(entry[0],"%H:%M")
                start_time = timedelta(hours=t.hour, minutes=t.minute)
                duration = timedelta(minutes=int(entry[1]))
                end_time = start_time + duration
                if selected_shift.get() == 3 and len(str(end_time)) > 9:
                    end_time_tmp = str(end_time)[7:]
                else:
                    end_time_tmp = str(end_time)
                end_time_format = datetime.strptime(end_time_tmp, "%H:%M:%S")
                end_time_format_tmp = str(end_time_format)
                end_time_format_str = end_time_format_tmp[11:16]
                report_string = []
                if entry[7] != "":
                    if entry[9] == "" and entry[10] == "":
                        report_string = f"User: {entry[2]}, pos: {entry[3]}, dept: {entry[4]}<br>Inventory code: {entry[5]}<br>Problem: {entry[6]}<br>Reason: {entry[7]}<br>Solution: {entry[8]}" 
                    else:
                        report_string = f"User: {entry[2]}, pos: {entry[3]}, dept: {entry[4]}<br>Inventory code: {entry[5]}<br>Problem: {entry[6]}<br>Reason: {entry[7]}<br>Solution: {entry[8]}<br>Old: {entry[9]}<br>New: {entry[10]}" 
                if entry[7] == "":
                    if entry[9] == "" and entry[10] == "":
                        report_string = f"User: {entry[2]}, pos: {entry[3]}, dept: {entry[4]}<br>Inventory code: {entry[5]}<br>Problem: {entry[6]}<br>Solution: {entry[8]}" 
                    else:
                        report_string = f"User: {entry[2]}, pos: {entry[3]}, dept: {entry[4]}<br>Inventory code: {entry[5]}<br>Problem: {entry[6]}<br>Solution: {entry[8]}<br>Old: {entry[9]}<br>New: {entry[10]}" 
                if entry[6] == "" and entry[7] == "":
                    if entry[9] == "" and entry[10] == "":
                        report_string = f"User: {entry[2]}, pos: {entry[3]}, dept: {entry[4]}<br>Inventory code: {entry[5]}<br>Solution: {entry[8]}"
                    else:
                        report_string = f"User: {entry[2]}, pos: {entry[3]}, dept: {entry[4]}<br>Inventory code: {entry[5]}<br>Solution: {entry[8]}<br>Old: {entry[9]}<br>New: {entry[10]}"          
            html = html + "<tr>"
            html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>"+entry[0]+"</td>"
            html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>"+end_time_format_str+"</td>"
            html = html + "<td style='border:1px solid black; text-align:left; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>"+report_string+"</td>"
            html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>&nbsp;</td>"
            html = html + "</tr>"
    if selected_shift.get() == 1:
        html = html + "<tr>"                       
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>14:30</td>"                
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>14:45</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>Discuss and hand over job to next shift</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>&nbsp;</td>"
        html = html + "</tr>"
        html = html + "<tr>"                       
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>14:45</td>"                
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>15:00</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>Made and sent Time Sheet Report to team leader</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>&nbsp;</td>"
        html = html + "</tr>"
    if selected_shift.get() == 2:
        html = html + "<tr>"                       
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>22:30</td>"                
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>22:45</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>Discuss and hand over job to next shift</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>&nbsp;</td>"
        html = html + "</tr>"
        html = html + "<tr>"                       
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>22:45</td>"                
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>23:00</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>Made and sent Time Sheet Report to team leader</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>&nbsp;</td>"
        html = html + "</tr>"
    if selected_shift.get() == 3:
        html = html + "<tr>"                       
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>06:30</td>"                
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>06:45</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>Discuss and hand over job to next shift</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>&nbsp;</td>"
        html = html + "</tr>"
        html = html + "<tr>"                       
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>06:45</td>"                
        html = html + "<td style='border:1px solid black; text-align:center; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>07:00</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>Made and sent Time Sheet Report to team leader</td>"
        html = html + "<td style='border:1px solid black; vertical-align:middle; font-family:&quot;Liberation Sans1&quot;'>&nbsp;</td>"
        html = html + "</tr>"
    html = html + "</tbody>"
    html = html + "</table>"                   
    html = html + "</body>"                   
    html = html + "</html>"                        
    
    leaders = [selected_leader_1, selected_leader_2, selected_leader_3, selected_leader_4,selected_leader_5, selected_leader_6, selected_leader_7, selected_leader_8]
    emails = ["jameslee@sms-vn.com", "trinhhuynh@sms-vn.com", "luantran@sms-vn.com", "hieu@sms-vn.com", "thao@sms-vn.com", "chay@sms-vn.com", "Nhan.Vo@sms-vn.com", "thinhnguyen@sms-vn.com"]

    recipients = [mail_username_value.get()+"@sms-vn.com"]

    for i in range(8):
        if (leaders[i].get()==1):
            recipients.append(emails[i])

    # Set up the email addresses and password. Please replace below with your email address and password
    email_from = mail_username_value.get()+"@sms-vn.com"
    password = mail_password_value.get()
    email_to = ",".join(recipients)
    # Generate today's date to be included in the email Subject
    date_str = selected_year.get() + selected_month.get() + selected_day.get()
    # Create a MIMEMultipart class, and set up the From, To, Subject fields
    email_message = MIMEMultipart()
    email_message['From'] = email_from
    email_message['To'] = email_to
    email_message['Subject'] = f'{date_str} Time Sheet Report - {username_value.get()}'

    # Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
    email_message.attach(MIMEText(html, "html"))
    # Convert it as a string
    email_string = email_message.as_string()
    
    # Connect to the Gmail SMTP server and Send Email
    
    try:
        with smtplib.SMTP_SSL("mail.sms-vn.com", 465) as server:
            server.login(email_from, password)
            server.sendmail(email_from, email_to.split(","), email_string)
        messagebox.showinfo("Info", "Your mail was sent successfully!")
        window.destroy()
    except:
        messagebox.showerror("Error", "Could not send the email! Please check your email username password carefully!")
        
                               
submit_frm = Frame(login_fr)
submit_frm.pack(pady=5)
submit_btn = Button(submit_frm, text = "   CLICK TO COMPLETE!!!   ", command = wr_submit)
submit_btn.pack()

window.title("Time Sheet Automation")
window.eval('tk::PlaceWindow . center')
window.mainloop()