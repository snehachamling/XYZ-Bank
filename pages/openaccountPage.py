from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class openAccount:
    def __init__(self, driver):
        self.driver = driver

    def bankmanager_login(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/button")

    def click_bankmanager_login(self):
        self.bankmanager_login().click()

    def open_account(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/button[2]")

    def click_open_account(self):
        self.open_account().click()

    def customer_name(self):
        return self.driver.find_element(By.ID, "userSelect")

    def click_customer_name(self):
        self.customer_name().click()

    def currency(self):
        return self.driver.find_element(By.ID,"currency")

    def click_currency(self):
        self.currency().click()

    def proceed_button(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/button")

    def click_proceed_button(self):
        self.proceed_button().click()

    def openAccount_page(self):
        self.click_bankmanager_login()
        self.click_open_account()


