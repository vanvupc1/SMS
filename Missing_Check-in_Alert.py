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
from selenium.webdriver.support.select import Select

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

from datetime import datetime, timedelta
import time

import schedule

from pygame import mixer

from threading import Thread
from threading import Event

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def get_data(username_content, password_content):
    #Sử dụng nhị phân mặc định của chrome thay vì chromedriver
    tmp = []
    while len(tmp) == 0:
        try:
            options = Options()
            options.binary_location = "C:\\Program Files\\Chrome\\sms_chrome.exe"
            options.add_experimental_option("detach", True)
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_argument('ignore-certificate-errors')
            options.headless = True
            service = Service(executable_path=resource_path('.\\driver\\chromedriver.exe'))
            driver = webdriver.Chrome(options = options, service = service)
            driver.get("https://hrm.sms-vn.com")
            username = driver.find_element(By.XPATH, value="//*[@id='formContainer']/div[1]/div[2]/input")
            username.send_keys(username_content)
            password = driver.find_element(By.XPATH, value="//*[@id='formContainer']/div[2]/div[2]/input")
            password.send_keys(password_content)
            submit = driver.find_element(By.XPATH, value="//*[@id='formContainer']/div[3]/input")
            submit.click()
            time.sleep(1)
            driver.execute_script("window.open('https://hrm.sms-vn.com/report/attendance', '1')")
            driver.switch_to.window("1")
            time.sleep(5)
            rows = driver.find_elements(By.XPATH, value="//*[@id='attendanceDetails']/tr")

            for i in range(len(rows)):
                name = driver.find_element(By.XPATH, value="//*[@id='attendanceDetails']/tr[" + "{}".format(i+1) + "]/td[6]")
                shift = driver.find_element(By.XPATH, value="//*[@id='attendanceDetails']/tr[" + "{}".format(i+1) + "]/td[7]")
                checkin = driver.find_element(By.XPATH, value="//*[@id='attendanceDetails']/tr[" + "{}".format(i+1) + "]/td[8]")
                checkout = driver.find_element(By.XPATH, value="//*[@id='attendanceDetails']/tr[" + "{}".format(i+1) + "]/td[9]")
                note = driver.find_element(By.XPATH, value="//*[@id='attendanceDetails']/tr[" + "{}".format(i+1) + "]/td[15]")
                tmp.extend((name.text, shift.text, checkin.text, checkout.text, note.text))

            driver.quit()
        except:
            pass

    entry_list = []
    s = 0
    while s < len(tmp):
        tmp1 = tmp[s:s+5]
        s=s+5
        entry_list.append(tmp1)
    on_duty_list = []
    for entry in entry_list:
        if entry[4] == "":
            on_duty_list.append(entry)
    return on_duty_list

def missing_check(staffs):
    risk = []
    for staff in staffs:
        if staff[2] == "":
            risk.append(staff[0])
    if len(risk) != 0:
        risk_string = risk[0]
        if len(risk) > 1:
            for i in range(1, len(risk)):
                risk_string += f", {risk[i]}"
        def play_sound(mixer1):
            mixer1.music.play(5)
            # ps.playsound("C:\\Users\\thinhnguyen\\Desktop\\warning.mp3")
            
        mixer.init()
        mixer.music.load(resource_path('.\\sound\\warning.mp3'))
        thread = Thread(target=play_sound, args = (mixer, ))
        thread.start()
        window = tk.Tk()
        window.geometry("550x80")
        window.resizable(False, False)
        content_fr = Frame(window)
        content_fr.pack()
        lbl_text = Label(content_fr, text="Haven't yet got data from ")
        lbl_text.pack(side=LEFT, pady=5)
        lbl_warning = Label(content_fr,text=f"{risk_string}", font=("Arial", 12), foreground="red")
        lbl_warning.pack(side = LEFT, pady=5)
        def stop_play_sound(mixer1):
            mixer1.music.stop()
            window.destroy()
        btn_ok = Button(window, text="OK", width=8, command=lambda : stop_play_sound(mixer))
        btn_ok.pack(pady=5)
        window.title("Missing Check-in Warning!!!")
        window.eval('tk::PlaceWindow . center')
        window.focus()
        window.mainloop()
        thread.join()

account_list = ["03006", "Abcd@1234", "03076", "03076", "01772", "8854526"]

def missing_check_morning():
    i = 0
    morning = []
    while i < 5:
        current_data = get_data(account_list[i], account_list[i+1])
        for item in current_data:
            if item[1] == "06 >15":
                morning.append(item)
        if len(morning) != 0:
            break
        else:
            i+=2
    missing_check(morning)

def missing_check_office_time():
    i = 0
    office_time = []
    while i < 5:
        current_data = get_data(account_list[i], account_list[i+1])
        for item in current_data:
            if item[1] == "08 >17" or item[1] == "08 >17 (GO)":
                office_time.append(item)
        if len(office_time) != 0:
            break
        else:
            i+=2
    missing_check(office_time)

def missing_check_afternoon():
    i = 0
    afternoon = []
    while i < 5:
        current_data = get_data(account_list[i], account_list[i+1])
        for item in current_data:
            if item[1] == "14 >23":
                afternoon.append(item)
        if len(afternoon) != 0:
            break
        else:
            i+=2
    missing_check(afternoon)

def missing_check_night():
    i = 0
    night = []
    while i < 5:
        current_data = get_data(account_list[i], account_list[i+1])
        for item in current_data:
            if item[1] == "22 >07":
                night.append(item)
        if len(night) != 0:
            break
        else:
            i+=2
    missing_check(night)

schedule.every().day.at("05:57").do(missing_check_morning)
schedule.every().day.at("07:57").do(missing_check_office_time)
schedule.every().day.at("13:57").do(missing_check_afternoon)
schedule.every().day.at("21:57").do(missing_check_night)

while True:
    schedule.run_pending()
    time.sleep(1)

