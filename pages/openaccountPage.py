from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class OpenAccount:
    def __init__(self,driver):
        self.driver = driver

    def bankmanager_login_text(self):
        wait = WebDriverWait(self.driver, 10)
        title = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/button")))
        return title.text

    def bankmanager_login(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/button")))

    def click_bankmanager_login(self):
        self.bankmanager_login().click()

    def openaccount_text(self):
        wait = WebDriverWait(self.driver, 10)
        title = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/button[2]")))
        return title.text

    def open_account(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]')))

    def click_open_account(self):
        self.open_account().click()

    def customer_text(self):
        wait = WebDriverWait(self.driver,10)
        title = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/label')))
        return title.text

    def customer_placeholder(self):
        select = Select(self.customer_name())
        return select.first_selected_option.text

    def customer_name(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((By.ID, "userSelect")))

    def currency_text(self):
        wait = WebDriverWait(self.driver, 10)
        title = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/label')))
        return title.text

    def currency_placeholder(self):
        select = Select(self.currency())
        return select.first_selected_option.text

    def currency(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((By.ID, "currency")))

    def process_button_text(self):
        wait = WebDriverWait(self.driver, 10)
        title = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/button")))
        return title.text

    def process_button(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/button")

    def click_process_button(self):
        self.process_button().click()

    def openaccountpage(self, customer_name, currency):
        self.click_bankmanager_login()
        self.click_open_account()

        if customer_name.strip():
            Select(self.customer_name()).select_by_visible_text(customer_name)
        if currency.strip():
            Select(self.currency()).select_by_visible_text(currency)
        self.click_process_button()