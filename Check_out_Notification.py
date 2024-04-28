import os
import sys
import telebot
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

apiToken = '6001083681:AAH_KfmFQH0ze01trxhuQWJgmFS4LHAi-JI'
chatID = '-1001544327787'
# apiURL = f'https://api.telegram.org/bot6001083681:AAH_KfmFQH0ze01trxhuQWJgmFS4LHAi-JI/sendMessage'

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
            # service = Service(executable_path=resource_path('.\\driver\\chromedriver.exe'))
            driver = webdriver.Chrome(options = options)
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

def get_data_previous(username_content, password_content):
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
            sel = Select(driver.find_element(By.XPATH, value="//*[@id='Date']"))
            sel.select_by_visible_text("Yesterday")
            choose = driver.find_element(By.XPATH, value="//*[@id='btnSubmit']")
            choose.click()
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
        if entry[4] == "" or entry[4] == "Missing Check-out":
            on_duty_list.append(entry)
    return on_duty_list

def checked_out(staffs):
    safe = []
    not_yet_out = []
    for staff in staffs:
        if staff[3] != "":
            safe.append(staff[0])
            safe.append(staff[3])
        else:
            not_yet_out.append(staff)
    index = 0
    bot = telebot.TeleBot(token=apiToken)
    while index < len(safe):
        message = f"{safe[index]} checked-out at {safe[index+1]}!"
        bot.send_message(chatID, message)
        index += 2
    if len(not_yet_out) != 0:
        for person in not_yet_out:
            message = f"Haven't got check-out data from {person[0]}"
            bot.send_message(chatID, message)
    return not_yet_out

account_list = ["03006", "Abcd@1234", "03076", "03076", "01772", "8854526"]

def checked_out_morning():
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
    flag = checked_out(morning)
    return flag

def checked_out_office_time():
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
    flag = checked_out(office_time)
    return flag

def checked_out_afternoon():
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
    flag = checked_out(afternoon)
    return flag

def checked_out_night():
    i = 0
    night = []
    while i < 5:
        current_data = get_data_previous(account_list[i], account_list[i+1])
        for item in current_data:
            if item[1] == "22 >07":
                night.append(item)
        if len(night) != 0:
            break
        else:
            i+=2
    flag = checked_out(night)
    return flag

def recheck_morning():
    global recheck_data_morning
    i = 0
    need_to_check = []
    while i < 5:
        current_data = get_data(account_list[i], account_list[i+1])
        for staff_1 in current_data:
            for staff_2 in recheck_data_morning:
                if staff_1[0] == staff_2[0]:
                    need_to_check.append(staff_1)
        if len(need_to_check) != 0:
            break
        else:
            i+=2
    recheck_data_morning = checked_out(need_to_check)

def recheck_office_time():
    global recheck_data_office_time
    i = 0
    need_to_check = []
    while i < 5:
        current_data = get_data(account_list[i], account_list[i+1])
        for staff_1 in current_data:
            for staff_2 in recheck_data_office_time:
                if staff_1[0] == staff_2[0]:
                    need_to_check.append(staff_1)
        if len(need_to_check) != 0:
            break
        else:
            i+=2
    recheck_data_office_time = checked_out(need_to_check)

def recheck_afternoon_before_midnight():
    global recheck_data_afternoon
    i = 0
    need_to_check = []
    while i < 5:
        current_data = get_data(account_list[i], account_list[i+1])
        for staff_1 in current_data:
            for staff_2 in recheck_data_afternoon:
                if staff_1[0] == staff_2[0]:
                    need_to_check.append(staff_1)
        if len(need_to_check) != 0:
            break
        else:
            i+=2
    recheck_data_afternoon = checked_out(need_to_check)

def recheck_afternoon_after_midnight():
    global recheck_data_afternoon
    i = 0
    need_to_check = []
    while i < 5:
        current_data = get_data_previous(account_list[i], account_list[i+1])
        for staff_1 in current_data:
            for staff_2 in recheck_data_afternoon:
                if staff_1[0] == staff_2[0]:
                    need_to_check.append(staff_1)
        if len(need_to_check) != 0:
            break
        else:
            i+=2
    recheck_data_afternoon = checked_out(need_to_check)

def recheck_night():
    global recheck_data_night
    i = 0
    need_to_check = []
    while i < 5:
        current_data = get_data_previous(account_list[i], account_list[i+1])
        for staff_1 in current_data:
            for staff_2 in recheck_data_night:
                if staff_1[0] == staff_2[0]:
                    need_to_check.append(staff_1)
        if len(need_to_check) != 0:
            break
        else:
            i+=2
    recheck_data_night = checked_out(need_to_check)

#Morning shift
def repeat(start_hour, start_minute, end_hour, end_minute, check):
    start_time = timedelta(hours=start_hour, minutes=start_minute)
    end_time = timedelta(hours=end_hour, minutes=end_minute)
    while start_time < end_time:
        delta = timedelta(minutes=15)
        start_time += delta
        if len(str(start_time)) > 9:
            schedule.every().day.at(str(datetime.strptime(str(start_time)[7:],"%H:%M:%S"))[11:16]).do(check)
        else:
            schedule.every().day.at(str(datetime.strptime(str(start_time),"%H:%M:%S"))[11:16]).do(check)

def all_were_out_morning():
    global recheck_data_morning
    recheck_data_morning = checked_out_morning()
    if len(recheck_data_morning) != 0:
        repeat(15, 0, 17, 0, recheck_morning)

def all_were_out_office_time():
    global recheck_data_office_time
    recheck_data_office_time = checked_out_office_time()
    if len(recheck_data_office_time) != 0:
        repeat(17, 0, 19, 0, recheck_office_time)

def all_were_out_afternoon():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    global recheck_data_afternoon
    recheck_data_afternoon = checked_out_afternoon()
    start = now.replace(hour = int(23), minute = int(0))
    end = now.replace(hour = int(23), minute = int(59))
    if len(recheck_data_afternoon) != 0:
        if now > start and now < end:
            repeat(23, 0, 23, 40, recheck_afternoon_before_midnight)
        else:
            repeat(23, 45, 25, 0, recheck_afternoon_after_midnight)

def all_were_out_night():
    global recheck_data_night
    recheck_data_night = checked_out_night()
    if len(recheck_data_night) != 0:
        repeat(7, 0, 9, 0, recheck_night)

schedule.every().day.at("15:10").do(all_were_out_morning)
schedule.every().day.at("17:10").do(all_were_out_office_time)
schedule.every().day.at("23:10").do(all_were_out_afternoon)
schedule.every().day.at("07:10").do(all_were_out_night)

while True:
    schedule.run_pending()
    time.sleep(1)

