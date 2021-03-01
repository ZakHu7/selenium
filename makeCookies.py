from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from webdriver_manager.chrome import ChromeDriverManager
from cred import username, password
import time

options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://warrior.uwaterloo.ca/')

print(driver.get_cookies())
driver.find_element_by_id('loginLink').click()
time.sleep(1)
driver.find_element_by_class_name('btn-soundcloud').click()


# Fill credentials
driver.find_element_by_id('userNameInput').send_keys(username)
driver.find_element_by_id('nextButton').click()
driver.find_element_by_id('passwordInput').send_keys(password)
driver.find_element_by_id('submitButton').click()
driver.switch_to.frame('duo_iframe')
time.sleep(1)
driver.find_element_by_name('dampen_choice').click()
driver.find_element_by_xpath('//*[@id="auth_methods"]/fieldset/div[1]/button').click()
                                            
time.sleep(10)            

driver.get('https://warrior.uwaterloo.ca/Program/GetProgramDetails?courseId=cc2a16d7-f148-461e-831d-7d4659726dd1&semesterId=26de9ca7-b227-429c-b21f-633b4cb4c462')
# driver.get('https://warrior.uwaterloo.ca/Program/GetProgramDetails?courseId=8e62544e-fe09-4953-8a45-1d26d0ff94f2&semesterId=26de9ca7-b227-429c-b21f-633b4cb4c462')

# 6 | click | css=div:nth-child(4) > .btn-primary | 
while True:
  try:
    #code with possible error
    time.sleep(0.2)
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > .btn-primary").click()
  except:
    driver.get('https://warrior.uwaterloo.ca/Program/GetProgramDetails?courseId=cc2a16d7-f148-461e-831d-7d4659726dd1&semesterId=26de9ca7-b227-429c-b21f-633b4cb4c462')
    continue
  else:
    #the rest of the code
    break

WebDriverWait(driver, 30000).until(expected_conditions.element_to_be_clickable((By.ID, "btnAccept")))
while True:
  try:
    # 7 | click | id=btnAccept | 
    driver.find_element(By.ID, "btnAccept").click()
  except:
    continue
  else:
    #the rest of the code
    break
# 8 | click | id=rbtnNo | 
driver.find_element(By.ID, "rbtnNo").click()
# 9 | click | css=.panel:nth-child(21) > .panel-body | 
driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(21) > .panel-body").click()
# 10 | click | css=.panel:nth-child(21) #rbtnNo | 
driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(21) #rbtnNo").click()
# 11 | click | css=.panel:nth-child(27) .radio-inline:nth-child(3) | 
driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(27) .radio-inline:nth-child(3)").click()
# 12 | click | css=.panel:nth-child(33) #rbtnNo | 
driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(33) #rbtnNo").click()
# 13 | click | css=.panel:nth-child(39) .radio-inline:nth-child(3) | 
driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(39) .radio-inline:nth-child(3)").click()
# 14 | click | css=.panel:nth-child(45) > .panel-body | 
driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(45) > .panel-body").click()
# 15 | click | css=.panel:nth-child(45) > .panel-body | 
driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(45) > .panel-body").click()
# 16 | click | css=.panel:nth-child(45) .radio-inline:nth-child(3) | 
driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(45) .radio-inline:nth-child(3)").click()
# 17 | click | css=.panel:nth-child(51) .radio-inline:nth-child(3) | 
driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(51) .radio-inline:nth-child(3)").click()
# 18 | click | css=.panel:nth-child(57) .radio-inline:nth-child(3) | 
driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(57) .radio-inline:nth-child(3)").click()
# 19 | click | css=.panel:nth-child(63) .radio-inline:nth-child(3) | 
driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(63) .radio-inline:nth-child(3)").click()
# 20 | click | css=.container-fluid > .btn-primary | 
driver.find_element(By.CSS_SELECTOR, ".container-fluid > .btn-primary").click()
# 21 | click | id=checkoutButton | 
driver.find_element(By.ID, "checkoutButton").click()
time.sleep(100)



# f = open("cookie.txt", "w")
# f.write(str(driver.get_cookies()).replace("\'", "\""))
# f.close()

# print(driver.get_cookies())
# driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/b/section/div[52]/div/div/a').click()