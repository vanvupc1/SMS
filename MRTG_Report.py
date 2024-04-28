from fpdf import FPDF

import base64
import os, shutil
import sys
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
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
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
## The pandas library is only for generating the current date, which is not necessary for sending emails

from datetime import datetime, timedelta

from PIL import Image

import time

window = tk.Tk()
window.geometry("310x120")
window.resizable(False, False)
login_fr = Frame(window)
login_fr.pack(pady=10)
username_parent_fr = Frame(login_fr)
username_parent_fr.pack(fill=X, expand=1)
username_fr = Frame(username_parent_fr)
username_fr.pack(side=LEFT, padx=25, expand=1, fill=X)
username_lbl =  Label(username_fr, text="Email:  ")
username_lbl.pack(side=LEFT)
username_value = tk.StringVar()
username_input = Entry(username_fr, textvariable = username_value, width=15)
username_input.pack(side=LEFT)
mail_tailer = Label(username_fr, text="@sms-vn.com")
mail_tailer.pack(side=LEFT)


password_parent_fr = Frame(login_fr)
password_parent_fr.pack(pady=10, fill=X, expand=1)
password_fr = Frame(password_parent_fr)
password_fr.pack(side=LEFT, padx=5)
password_lbl =  Label(password_fr, text="Password:  ")
password_lbl.pack(side=LEFT)
password_value = tk.StringVar()
password_input = Entry(password_fr, textvariable = password_value, show="*", width=30)
password_input.pack(side=LEFT)

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
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('ignore-certificate-errors')
    service = Service(executable_path=resource_path('.\\driver\\chromedriver.exe'))
    driver = webdriver.Chrome(options = options, service = service)
    driver.maximize_window()
    driver.get("https://cacti.jumbo98.com/index.php?login=true")

    username = driver.find_element(By.XPATH, value="//*[@id='login_username']")
    username.send_keys("noc")
    password = driver.find_element(By.XPATH, value="//*[@id='login_password']")
    password.send_keys("noc")
    submit = driver.find_element(By.XPATH, value="//*[@id='login']/div[2]/table/tbody/tr[4]/td/input")
    submit.click()
    driver.implicitly_wait(10)
    MBC = driver.find_element(By.XPATH, value="//*[@id='tree_anchor-112_anchor']")
    MBC.click()

    driver.execute_script("window.open('http://monitor.qtsc.com.vn/public/login.htm', '1')")
    driver.switch_to.window("1")
    login_name = driver.find_element(By.XPATH, value="//*[@id='loginusername']")
    login_name.send_keys("sms")
    password_qtsc = driver.find_element(By.XPATH, value="//*[@id='loginpassword']")
    password_qtsc.send_keys("Sms@123456")
    submit_qtsc = driver.find_element(By.XPATH, value="//*[@id='submitter1']")
    submit_qtsc.click()
    driver.implicitly_wait(10000)
    driver.execute_script("window.open('http://monitor.qtsc.com.vn/sensor.htm?id=21530&tabid=2', '1')")
    driver.execute_script("window.open('https://cacti.jumbo98.com/graph.php?local_graph_id=16552', '2')")
    driver.execute_script("window.open('https://cacti.jumbo98.com/graph.php?local_graph_id=3192', '3')")
    driver.execute_script("window.open('https://cacti.jumbo98.com/graph.php?local_graph_id=3194', '4')")
    driver.execute_script("window.open('https://cacti.jumbo98.com/graph.php?local_graph_id=3190', '5')")

    def get_image(list_image):
        for a in range(2,6):
            FET2 = driver.find_element(By.XPATH, value="/html/body/div[5]/div/main/table/tbody/tr["+"{}".format(a)+"]/td/table/tbody/tr[1]/td[1]/div/img")
            tmp = FET2.get_attribute("src")
            list_image.append(tmp[22:])

    # FET2_day = driver.find_element(By.XPATH, value="//*[@id='graph_16552']")
    # tmp = FET2_day.get_attribute("src")

    img_list = []

    driver.switch_to.window("2")
    get_image(img_list)
    driver.switch_to.window("3")
    get_image(img_list)
    driver.switch_to.window("4")
    get_image(img_list)
    driver.switch_to.window("5")
    get_image(img_list)    
    current_directory = os.getcwd()
    my_path = os.path.join(current_directory, r'tmp')
    if not os.path.exists(my_path):
        os.makedirs(my_path)

    i = 0

    for data in img_list:
        i = i + 1
        data_format = data.replace(' ', '+')
        imgdata = base64.b64decode(data_format)
        tmp_path = str(i) + ".jpeg"
        filename = os.path.join(my_path, tmp_path)  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)
    for t in range(1, 17):
        img_path = os.path.join(my_path, "{}".format(t)+".jpeg")
        img_path_2 = os.path.join(my_path, "{}".format(t)+".jpg")
        img = Image.open(img_path)
        img.save(img_path_2, quality=25)
    driver.switch_to.window("1")
    image1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/img")))
    actions = ActionChains(driver)
    actions.move_to_element(image1)
    save_path = os.path.join(my_path, "qtsc1.png")
    actions.perform()
    time.sleep(1)
    image1.screenshot(save_path)
    driver.get("http://monitor.qtsc.com.vn/sensor.htm?id=21530&tabid=3")
    image2 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/img")))
    actions.move_to_element(image2)
    save_path = os.path.join(my_path, "qtsc2.png")
    actions.perform()
    time.sleep(1)
    image2.screenshot(save_path)
    driver.get("http://monitor.qtsc.com.vn/sensor.htm?id=21530&tabid=4")
    image3 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/img")))
    actions.move_to_element(image3)
    save_path = os.path.join(my_path, "qtsc3.png")
    actions.perform()
    time.sleep(1)
    image3.screenshot(save_path)
    driver.get("http://monitor.qtsc.com.vn/sensor.htm?id=21530&tabid=5")
    image4 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/img")))
    actions.move_to_element(image4)
    save_path = os.path.join(my_path, "qtsc4.png")
    actions.perform()
    time.sleep(1)
    image4.screenshot(save_path)

    pdf = FPDF()
    pdf.set_auto_page_break(0)
    pdf.add_page()
    def make_title(title, title_top_padding, title_left_padding):
        pdf.set_font("Arial", "B", size=15)
        pdf.text(title_left_padding, title_top_padding, txt=title)
    def make_report(image_url, image_padding_top, frequency, frequency_padding):
        pdf.set_font("Arial", size=12)
        pdf.image(image_url, x= None, y=image_padding_top, w=190, h=70)
        pdf.text(frequency_padding, image_padding_top + 76, txt=frequency)
    
    image_padding_top_variables = [15, 107, 200, 15, 107, 200, 15, 107, 200, 15, 108, 200, 15, 107, 200, 15]
    temp = ["Daily (5 Minute Average)", "Weekly (30 Minute Average)", "Monthly (2 Hour Average)", "Yearly (1 Day Average)"]
    temp1 = temp + temp + temp + temp
    section = {9: "BGP_KBT [30M/50M]", 100: "IA_PCCW + MITIGATION [200M/1G]", 193: "IA_SINGTEL [20M/50M]",10: "IA_TWGATE [200M/600M]"}
    frequency_padding_left = 80
    for a in range(1, 17):
        image_path = os.path.join(my_path, "{}".format(a)+".jpg")
        make_report(image_path, image_padding_top_variables[a-1],temp1[a-1], frequency_padding_left)
        if (a==3 or a==6 or a==9 or a==12 or a==15):
            pdf.add_page()
        if a==1:
            left = 80
            make_title(section[9], 9, left)
        if a==5:
            left = 60
            make_title(section[100], 100, left)
        if a==8:
            left = 75
            make_title(section[193], 193, left)
        if a==13:
            left = 75
            make_title(section[10], 10, left)

    make_title("QTSC BANDWIDTH USAGE", 100, 70)
    make_title("202.78.228.64/26 - Traffic Total", 108, 65)
    qtsc_frequency = ["Live Data", "2 Days", "Monthly", "Yearly"]
    qtsc_image_top_padding = [112, 200, 15, 112]
    qtsc_frequency_padding_left = 95
    for x in range (1, 5):
        qtsc_image_path = os.path.join(my_path, "qtsc"+"{}".format(x)+".png")
        make_report(qtsc_image_path, qtsc_image_top_padding[x-1], qtsc_frequency[x-1], qtsc_frequency_padding_left)
        if x == 2:
            pdf.add_page()
    get_date = datetime.now()
    get_date_format = get_date.strftime("%Y")+get_date.strftime("%m")+get_date.strftime("%d")

    output_pdf = os.path.join(my_path, get_date_format+" MRTG & PRTG Report.pdf")
    pdf.output(output_pdf)

    #Send mail

    email_from = username_value.get()+"@sms-vn.com"
    password = password_value.get()
    recipients = "it-team@sms-vn.com, kwongyong@enpine.com"
    # Create a MIMEMultipart class, and set up the From, To, Subject fields
    email_message = MIMEMultipart()
    email_message['From'] = email_from
    email_message['To'] = recipients
    email_message['Subject'] = f'{get_date_format} MRTG & PRTG Report'

    attachment_pdf = email_message['Subject']+".pdf"

    # Attach the pdf to the msg going by e-mail
    with open(output_pdf, "rb") as f:
        #attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
        attach = MIMEApplication(f.read(),_subtype="pdf")
    attach.add_header('Content-Disposition','attachment',filename=attachment_pdf)

    # Add attachment to message and convert message to string
    email_message.attach(attach)

    # Connect to the Gmail SMTP server and Send Email
    
    try:
        with smtplib.SMTP_SSL("mail.sms-vn.com", 465) as server:
            server.login(email_from, password)
            server.sendmail(email_from, recipients.split(','), email_message.as_string())
        messagebox.showinfo("Info", "Your mail was sent successfully!")
        window.destroy()
    except:
        messagebox.showerror("Error", "Could not establish the connection! Please try again!")

    #Make the temporary folder empty
    for filename in os.listdir(my_path):
        file_path = os.path.join(my_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    os.rmdir(my_path)


submit_frm = Frame(login_fr)
submit_frm.pack(pady=5)
submit_btn = Button(submit_frm, text = "   CLICK TO COMPLETE!!!   ", command = wr_submit)
submit_btn.pack()

window.title("MRTG & PRTG Report")
window.eval('tk::PlaceWindow . center')
window.mainloop()