from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
                                                        
driver.get('https://warrior.uwaterloo.ca/Program/GetProgramDetails?courseId=cc2a16d7-f148-461e-831d-7d4659726dd1&semesterId=26de9ca7-b227-429c-b21f-633b4cb4c462')
f = open("cookie.txt", "w")
f.write(str(driver.get_cookies()).replace("\'", "\""))
f.close()

print(driver.get_cookies())
# driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/b/section/div[52]/div/div/a').click()