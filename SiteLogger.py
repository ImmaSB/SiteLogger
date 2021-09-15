from selenium import webdriver
import time
import os

usr = "your_username"
pw = "your_pw"

os.path['PATH'] =+ r"C:/SeleniumDriver"
driver = webdriver.chrome
driver.get("https://ies.edu.np/members/site/userlogin")
time.sleep(3)

username = driver.find_element_by_id("email")
username.send_keys(usr)
time.sleep(1)
password = driver.find_element_by_id("password")
password.send_keys(pw)

login = driver.find_element_by_class_name("btn")
login.click()

print("DONE!, program exiting in 3 seconds")
time.sleep(3)