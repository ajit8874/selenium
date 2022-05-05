# import selenium
import time

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# options = Options()
# options.add_argument("--window-size=1920,1080")
# driver = webdriver.Chrome(options=options)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome("/home/ajitsingh/Python/chromedriver_linux64/chromedriver")
driver.maximize_window()

driver.get("https://qa-candidates.phenompeople.com/dashboard/candidates")
print("dashboard")

# userid="username"
# driver.find_elements(By.ID("username"))
print("svd")
# driver.find_element(By.ID("username"))


# wait = WebDriverWait(driver, 10)
# wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary-signin"))).click()
# print("success2")


# element = WebDriverWait(driver, 10).until(
#     # EC.presence_of_element_located((By.ID, "username"))
#     EC.Element_to_be_selected(By.ID, "username")
# )

# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
# driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS)
time.sleep(10)



try:
    # driver.find_element(By.ID("username"))
    # driver.find_element_by_id("username").click()
    element=driver.find_element_by_id("username")

except:
    print("element does not fount")


# try:
#     # wait 10 seconds before looking for element
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "btn-primary-signin"))
#     )
# finally:
#     # else quit
#     driver.quit()



#
# driver.find_element_by_id("username").send_keys("teresa.vulluri@phenompeople.com")
# print("aa")
#
# driver.find_element_by_class_name("btn-primary-signin").click()



# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME ("btn-primary-signin"))).click())
# driver

