from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomersPage:
    def __init__(self,driver):
        self.driver = driver

    def bankmanager_login(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/button")))

    def click_bankmanager_login(self):
        self.bankmanager_login().click()

    def customers(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/button[3]")))

    def click_customers(self):
        self.customers().click()

    def search_customers(self):
        wait = WebDriverWait(self.driver,10)
        return wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/form/div/div/input')))

    def enter_search_customers(self,customer_name):
        self.search_customers().send_keys(customer_name)

    def clear_search(self):
        self.search_customers().clear()

    def delete_customer(self):
        wait = WebDriverWait(self.driver,10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr[1]/td[5]/button')))

    def click_delete_customer(self):
        self.delete_customer().click()

    def customerpage(self,customer_name):
        self.click_bankmanager_login()
        self.click_customers()
        self.enter_search_customers(customer_name)
        self.clear_search()
        self.click_delete_customer()


