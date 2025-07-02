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
open_account = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/button[2]")))
open_account.click()
customer_name = wait.until(EC.element_to_be_clickable((By.ID, "userSelect")))
customer_name.click()
select_customer = Select(customer_name)
select_customer.select_by_visible_text("Harry Potter")
currency = driver.find_element(By.ID,"currency")
currency.click()
# select_currency = Select(currency)
# select_currency.select_by_visible_text("Dollar")
proceed_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/button")
proceed_button.click()

# alert = driver.switch_to.alert
# actual_result = alert.text
# expected_result_contains = "Account created successfully with account Number :"
# print("Account created successfully")
# alert.accept()

validation_msg = currency.get_attribute("validationMessage")
print("Validation message:", validation_msg)
expected_msg = "Please select an item in the list."
assert validation_msg == expected_msg, "Validation message mismatch"


time.sleep(5)
