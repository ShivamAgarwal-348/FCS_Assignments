#FCS Assignment 2, question 3
#Name: Shivam Agarwal
#Roll number: 2020123

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = 'C:\Development\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path)
domain = 'iiitd.edu.in'
driver.get('https://dnsdumpster.com/')
time.sleep(2)
driver.implicitly_wait(30)
search = driver.find_element(By.ID, 'regularInput')
search.send_keys(domain + '\n')

data = driver.find_elements(By.CSS_SELECTOR,'.table-responsive')
host = data[3]

names = host.find_elements(By.CLASS_NAME, 'col-md-4')
ips = host.find_elements(By.CLASS_NAME, 'col-md-3')

subdomains = []
priv_ips = []
for name in names:
    # print(name.text.split('\n')[0])
    subdomains.append(name.text.split('\n')[0])

a = 0
for ip in ips:
    if a%2 == 1:
        a+=1
        continue
    # print(ip.text.split('\n')[0])
    priv_ips.append(ip.text.split('\n')[0])
    a += 1
# print(len(subdomains))
# print(len(priv_ips))
submission = []
for i in range(len(subdomains)):
    submission.append((subdomains[i],priv_ips[i]))
print(submission)










