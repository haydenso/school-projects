from selenium import webdriver
import pyautogui
import time

driver = webdriver.Chrome()
driver.get('https://meet.google.com/_meet')

sign_in = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[2]/div/div[2]/div/span/span')
sign_in.click()

gmail = driver.find_element_by_xpath('//*[@id="identifierId"]')
gmail.send_keys('')                                                             # SCHOOL GMAIL

Next = driver.find_element_by_xpath('//*[@id="identifierNext"]/span')
Next.click()

driver.get('https://sc.lg.esf.edu.hk/login/index.php?SAMLRequest=fVLJTsMwEL0j8Q%2BW71mFAFlNUAEhKrFENHDgZuxJY9UZB4%2FTwt%2BTpiDgANfnN28Zz%2BzsrbNsA56Mw4JnccoZoHLa4Krgj%2FVVdMrPysODGcnO9mI%2BhBYf4HUACmycRBLTQ8EHj8JJMiRQdkAiKLGc396IPE5F711wylnOFpcFb1plZSPBtmuzejG6R3BatbrvXd9alGupOi3XyNnTV6x8F2tBNMACKUgMI5TmaZTmUXZSp6k4ykR%2B%2FMxZ9el0bnDf4L9YL3sSieu6rqLqfllPAhujwd%2BN7IKvnFtZiJXrdvaVJDKbEW6kJeBsTgQ%2BjAEvHNLQgV%2BC3xgFjw83BW9D6EkkyXa7jb9lEplQUA6tQYhBD3G7TqQiXk77FVNF%2F2Ox%2FxeQXwF4%2BW0xS35IlZ%2F%2FtquzuKycNeqdza112wsPMoxdgh%2FGKlfOdzL87ZbF2YQYHTUTVQxIPSjTGNCcJeXe9feBjGfzAQ%3D%3D&RelayState=https%3A%2F%2Faccounts.google.com%2FCheckCookie%3Fcontinue%3Dhttps%253A%252F%252Fmeet.google.com%252F_meet%26hl%3Den%26checkedDomains%3Dyoutube%26checkConnection%3Dyoutube%253A181%253A1%26pstMsg%3D1')

username = driver.find_element_by_xpath('//*[@id="username"]').send_keys('')    #SMART USERNAME

password = driver.find_element_by_xpath('//*[@id="password"]').send_keys('')    #SMART PASSWORD

enter = driver.find_element_by_xpath('//*[@id="loginbtn"]')
enter.click()

cont = driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div')
cont.click()


time.sleep(4)
pyautogui.click((1225, 646))       # click on call
time.sleep(4)
pyautogui.click((642, 151))       # close notif
time.sleep(2)
pyautogui.click((642, 151))       # block camera and mic
time.sleep(2)
pyautogui.click((1105, 705))       # join call
time.sleep(2)
pyautogui.click((1056, 442))         # close join others
time.sleep(2)
pyautogui.click((642, 151))           # close another notif
time.sleep(2)
pyautogui.click((595, 262))             # block
time.sleep(2)
pyautogui.click((595, 262))             # block
time.sleep(5)
pyautogui.click((1105, 705))          # join call

time.sleep(6)

# driver.quit()                    # close window
