import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

wait = WebDriverWait(driver, 10)
bank_manager_login = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/button")))
bank_manager_login.click()
customers = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/button[3]")))
customers.click()
search_customers = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/form/div/div/input")))
search_customers.send_keys("Harry")
time.sleep(2)
search_customers.clear()
delete_customers = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr[5]/td[5]/button")))
delete_customers.click()

time.sleep(5)
