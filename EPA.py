import os
import sys
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
#Keys được dùng cho các thao tác dùng nút trên bàn phím (Ctrl, ALT,...)
from selenium.webdriver.common.by import By
#Thuộc tính By dùng để định vị các element (Ex: By.ID, By.Name, By.XPATH,...)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains


from anyascii import *
#Thư viện anyascii dùng để chuẩn hóa chuỗi


def epa_submit(ID,PW):
    #Sử dụng nhị phân mặc định của chrome thay vì chromedriver


    #Sử dụng nhị phân mặc định của chrome thay vì chromedriver
    options = Options()
    options.binary_location = "C:\\Program Files (x86)\\SMS Chrome\\sms_chrome.exe"
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options = options)
    driver.get("https://epa.sms-vn.com")
    #Định vị element username, password theo ID
    username = driver.find_element(By.ID, "Username")
    username.send_keys(ID)
    password = driver.find_element(By.ID, "Password")
    password.send_keys(PW)

    #Định vị nút login theo tên bằng XPATH
    login = driver.find_element(By.XPATH, value="//input[@name='submit']")
    login.click()

    #Sử dụng WebDriverWait để tạo ra thời gian chờ (time out = 20) cho các element cần định vị load xong, kèm theo sau là phương thức xử lí
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='EPATab']/ul/li[@heading='Monthly EPAs']"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//table/tbody/tr[2]/td[5]/a"))).click()

    #-----Get the comment-----

    tmp = [];

    for i in range(1,15):
        xpath_extend = "//div[@class='panel-body']/table/tbody["+"{}".format(i)+"]/tr[1]/td[4]/div/a"
        xpath_getvalue = "//div[@class='panel-body']/table/tbody["+"{}".format(i)+"]/tr[1]/td[4]/div"
        driver.implicitly_wait(10)
        epa = driver.find_element(By.XPATH, value=xpath_getvalue)
        if "...more" not in epa.text:
            tmp.append(epa.text)
        else:
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_extend))))
            epa= driver.find_element(By.XPATH, value=xpath_getvalue)
            tmp.append(epa.text)

        # tmp.append(epa.text)

    for i  in range(1, 4):
        xpath_extend_1="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][2]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-1']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope oddRow']["+"{}".format(i)+"]/tr[@class='ng-scope'][1]/td[@class='col-comment'][1]/div[@class='ng-binding']/a"
        xpath_extend_2="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][2]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-1']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope evenRow']["+"{}".format(i)+"]/tr[@class='ng-scope'][1]/td[@class='col-comment'][1]/div[@class='ng-binding']/a"
        xpath_getvalue_1="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][2]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-1']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope oddRow']["+"{}".format(i)+"]/tr[@class='ng-scope'][1]/td[@class='col-comment'][1]/div[@class='ng-binding']"
        xpath_getvalue_2="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][2]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-1']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope evenRow']["+"{}".format(i)+"]/tr[@class='ng-scope'][1]/td[@class='col-comment'][1]/div[@class='ng-binding']"
        driver.implicitly_wait(10)
        epa_1 = driver.find_element(By.XPATH, value=xpath_getvalue_1)
        driver.implicitly_wait(10)
        epa_2 = driver.find_element(By.XPATH, value=xpath_getvalue_2)
        if "...more" not in epa_1.text:
            tmp.append(epa_1.text)
        else:
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_extend_1))))
            epa1 = driver.find_element(By.XPATH, xpath_getvalue_1)
            tmp.append(epa_1.text)
        if "...more" not in epa_2.text:
            tmp.append(epa_2.text)
        else:
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_extend_2))))
            epa_2 = driver.find_element(By.XPATH, xpath_getvalue_2)
            tmp.append(epa_2.text)

    for i  in range(1, 3):                  
        xpath_extend_1="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][3]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-2']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope oddRow']["+"{}".format(i)+"]/tr[@class='ng-scope'][1]/td[@class='col-comment'][1]/div[@class='ng-binding']/a"
        xpath_extend_2="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][3]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-2']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope evenRow']["+"{}".format(i)+"]/tr[@class='ng-scope'][1]/td[@class='col-comment'][1]/div[@class='ng-binding']/a"
        xpath_getvalue_1="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][3]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-2']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope oddRow']["+"{}".format(i)+"]/tr[@class='ng-scope'][1]/td[@class='col-comment'][1]/div[@class='ng-binding']"
        xpath_getvalue_2="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][3]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-2']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope evenRow']["+"{}".format(i)+"]/tr[@class='ng-scope'][1]/td[@class='col-comment'][1]/div[@class='ng-binding']"
        driver.implicitly_wait(10)
        epa_1 = driver.find_element(By.XPATH, value=xpath_getvalue_1)
        driver.implicitly_wait(10)
        epa_2 = driver.find_element(By.XPATH, value=xpath_getvalue_2)
        if "...more" not in epa_1.text:
            tmp.append(epa_1.text)
        else:
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_extend_1))))
            epa1 = driver.find_element(By.XPATH, xpath_getvalue_1)
            tmp.append(epa_1.text)
        if "...more" not in epa_2.text:
            tmp.append(epa_2.text)
        else:
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_extend_2))))
            epa_2 = driver.find_element(By.XPATH, xpath_getvalue_2)
            tmp.append(epa_2.text)
        if i == 2:
            xpath_extend_3="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][3]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-2']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope oddRow']["+"{}".format(i+1)+"]/tr[@class='ng-scope'][1]/td[@class='col-comment'][1]/div[@class='ng-binding']/a"
            xpath_getvalue_3="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][3]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-2']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope oddRow']["+"{}".format(i+1)+"]/tr[@class='ng-scope'][1]/td[@class='col-comment'][1]/div[@class='ng-binding']"
            epa_3 = driver.find_element(By.XPATH, value=xpath_getvalue_3)
            driver.implicitly_wait(10)
            if "...more" not in epa_3.text:
                tmp.append(epa_3.text)
            else:
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_extend_3))))
                epa1 = driver.find_element(By.XPATH, xpath_getvalue_3)
                tmp.append(epa_3.text)


    tmp1 = []

    for i in range(len(tmp)):
        if " less" not in tmp[i]:
            tmp1.append(anyascii(tmp[i]))
        else:
            tmp1.append(anyascii(tmp[i].removesuffix(' less')))

    #-----Get the score-----

    tmp2 = []

    for i in range(1, 8):
        driver.implicitly_wait(10)
        score1=driver.find_element(By.XPATH, value = "/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][1]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-0']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope oddRow']["+"{}".format(i)+"]/tr[@class='ng-scope'][1]/td[@class='text-center col-score-star'][1]/div[1]/div/span[@class='score-star-rating']/span[@class='ng-binding']")
        score2=driver.find_element(By.XPATH, value = "/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][1]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-0']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope evenRow']["+"{}".format(i)+"]/tr[@class='ng-scope'][1]/td[@class='text-center col-score-star'][1]/div[1]/div/span[@class='score-star-rating']/span[@class='ng-binding']")
        tmp2.append(score1.text)
        tmp2.append(score2.text)

    for i in range(1, 4):
        driver.implicitly_wait(10)
        score1=driver.find_element(By.XPATH, value = "/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][2]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-1']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope oddRow']["+"{}".format(i)+"]/tr[@class='ng-scope'][1]/td[@class='text-center col-score-star'][1]/div[1]/div/span[@class='score-star-rating']/span[@class='ng-binding']")
        score2=driver.find_element(By.XPATH, value = "/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][2]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-1']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope evenRow']["+"{}".format(i)+"]/tr[@class='ng-scope'][1]/td[@class='text-center col-score-star'][1]/div[1]/div/span[@class='score-star-rating']/span[@class='ng-binding']")
        tmp2.append(score1.text)
        tmp2.append(score2.text)

    for i in range(1, 3):
        driver.implicitly_wait(10)
        score1=driver.find_element(By.XPATH, value="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][3]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-2']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope oddRow']["+"{}".format(i)+"]/tr[@class='ng-scope'][1]/td[@class='text-center col-score-star'][1]/div[1]/div/span[@class='score-star-rating']/span[@class='ng-binding']")
        score2=driver.find_element(By.XPATH, value="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][3]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-2']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope evenRow']["+"{}".format(i)+"]/tr[@class='ng-scope'][1]/td[@class='text-center col-score-star'][1]/div[1]/div/span[@class='score-star-rating']/span[@class='ng-binding']")
        tmp2.append(score1.text)
        tmp2.append(score2.text)
        if i == 2:
            score1=driver.find_element(By.XPATH, value="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/any[2]/any[@class='ng-scope']/epa-performance-detail[@class='ng-isolate-scope']/div[@class='ng-scope'][3]/div[@class='panel panel-default']/div[@class='panel-collapse collapse in kpiGroup-2']/div[@class='panel-body']/table[@class='row table table-bordered table-striped table-performance-detail table-custom']/tbody[@class='ng-scope oddRow']["+"{}".format(i+1)+"]/tr[@class='ng-scope'][1]/td[@class='text-center col-score-star'][1]/div[1]/div/span[@class='score-star-rating']/span[@class='ng-binding']") 
            tmp2.append(score1.text)

    driver.back()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='EPATab']/ul/li[@heading='Monthly EPAs']"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//table/tbody/tr[1]/td[5]/a"))).click()
  
    my_answer = driver.find_element(By.XPATH, value="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/div[@class='ng-scope']/div[@class='evaluation-detail ng-scope']/div[@class='kpi-group-item-wrapper ng-scope'][1]/div[@class='kpi-item-wrapper panel-collapse collapse in kpi-group-0'][1]/div[@class='comment-wrapper ng-scope']/div[@class='panel-collapse collapse in kpi-comment-0-0']/textarea[1]")
    my_answer.send_keys(tmp1[0])
    for i in range(1, 14):
        my_answer = driver.find_element(By.XPATH, value="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/div[@class='ng-scope']/div[@class='evaluation-detail ng-scope']/div[@class='kpi-group-item-wrapper ng-scope'][1]/div[@class='kpi-item-wrapper panel-collapse collapse in kpi-group-0']["+"{}".format(i+1)+"]/div[@class='comment-wrapper ng-scope']/div[@class='panel-collapse collapse in kpi-comment-"+"{}".format(i)+"-"+"{}".format(i)+"']/textarea[@class='form-control ng-pristine ng-untouched ng-valid ng-empty ng-valid-maxlength']")
        my_answer.send_keys(tmp1[i])
    
    my_answer = driver.find_element(By.XPATH, value="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/div[@class='ng-scope']/div[@class='evaluation-detail ng-scope']/div[@class='kpi-group-item-wrapper ng-scope'][2]/div[@class='kpi-item-wrapper panel-collapse collapse in kpi-group-1'][1]/div[@class='comment-wrapper ng-scope']/div[2]/textarea[1]")
    my_answer.send_keys(tmp1[14])
    for i in range(15, 20):
        my_answer = driver.find_element(By.XPATH, value="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/div[@class='ng-scope']/div[@class='evaluation-detail ng-scope']/div[@class='kpi-group-item-wrapper ng-scope'][2]/div[@class='kpi-item-wrapper panel-collapse collapse in kpi-group-1']["+"{}".format(i-13)+"]/div[@class='comment-wrapper ng-scope']/div[2]/textarea[1]")
        my_answer.send_keys(tmp1[i])
    my_answer = driver.find_element(By.XPATH, value="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/div[@class='ng-scope']/div[@class='evaluation-detail ng-scope']/div[@class='kpi-group-item-wrapper ng-scope'][3]/div[@class='kpi-item-wrapper panel-collapse collapse in kpi-group-2'][1]/div[@class='comment-wrapper ng-scope']/div[2]/textarea[1]")
    my_answer.send_keys(tmp1[20])

    for i in range(21, 25):
        my_answer = driver.find_element(By.XPATH, value="/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/div[@class='ng-scope']/div[@class='evaluation-detail ng-scope']/div[@class='kpi-group-item-wrapper ng-scope'][3]/div[@class='kpi-item-wrapper panel-collapse collapse in kpi-group-2']["+"{}".format(i-19)+"]/div[@class='comment-wrapper ng-scope']/div[2]/textarea[1]")
        my_answer.send_keys(tmp1[i])


    for i in range(14):
        star =  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/div[@class='ng-scope']/div[@class='evaluation-detail ng-scope']/div[@class='kpi-group-item-wrapper ng-scope'][1]/div[@class='kpi-item-wrapper panel-collapse collapse in kpi-group-0']["+"{}".format(i+1)+"]/div[@class='kpi-wrapper']/div[@class='rating-by-star ng-scope']/div[@class='rating-form']/div[@class='rating-container rating-xs rating-animate']/div[@class='rating']/span[@class='empty-stars']/span[@class='star']["+"{}".format(tmp2[i])+"]/i[@class='glyphicon glyphicon-star-empty']")))
        driver.execute_script("arguments[0].scrollIntoView();", star)
        star.click()
    for i in range(14, 20):
        star =  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/div[@class='ng-scope']/div[@class='evaluation-detail ng-scope']/div[@class='kpi-group-item-wrapper ng-scope'][2]/div[@class='kpi-item-wrapper panel-collapse collapse in kpi-group-1']["+"{}".format(i-13)+"]/div[@class='kpi-wrapper']/div[@class='rating-by-star ng-scope']/div[@class='rating-form']/div[@class='rating-container rating-xs rating-animate']/div[@class='rating']/span[@class='empty-stars']/span["+"{}".format(tmp2[i])+"]")))
        driver.execute_script("arguments[0].scrollIntoView();", star)
        star.click()
    for i in range(20, 25):
        star =  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html[@class='ng-scope']/body/div[@class='container-fluid page']/div[@class='row']/div[@class='ng-scope']/div[@class='ng-scope']/div[@class='col-sm-12']/div[@class='row epa-form']/div[@class='ng-scope']/div[@class='evaluation-detail ng-scope']/div[@class='kpi-group-item-wrapper ng-scope'][3]/div[@class='kpi-item-wrapper panel-collapse collapse in kpi-group-2']["+"{}".format(i-19)+"]/div[@class='kpi-wrapper']/div[@class='rating-by-star ng-scope']/div[@class='rating-form']/div[@class='rating-container rating-xs rating-animate']/div[@class='rating']/span[@class='empty-stars']/span["+"{}".format(tmp2[i])+"]")))
        driver.execute_script("arguments[0].scrollIntoView();", star)
        star.click()

    #Continue here!!!
