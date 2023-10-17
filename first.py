from selenium import webdriver
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

opt=ChromeOptions()
opt.add_experimental_option('detach',True)
#opt.add_argument('--headless')
driver=webdriver.Chrome(options=opt)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
actual_title=driver.title
exp_title="OrangeHRM"

if actual_title==exp-title:
    print(login Test passed)
else:
    print("failed")



opt=ChromeOptions()
opt.add_experimental_option('detach',True)
#opt.add_argument('--headless')
driver=webdriver.Chrome(options=opt)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
actual_title=driver.title
exp_title="OrangeHRM"

if actual_title==exp-title:
    print(login Test passed)
else:
    print("failed")




print("--------------Hello-------------------")

driver.close()
