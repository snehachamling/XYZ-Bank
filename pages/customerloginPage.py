from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomerloginPage:
    def __init__(self, driver):
        self.driver = driver

    def customer_login(self):
        wait = WebDriverWait(self.driver,10)
        return wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div[2]/div/div[1]/div[1]/button')))

    def click_customer_login(self):
        self.customer_login().click()

    def your_name(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.ID, "userSelect")))

    def login_button(self):
        return self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button')

    def click_login_button(self):
        self.login_button().click()

    def customerloginpage(self, your_name):
        self.click_customer_login()
        Select(self.your_name()).select_by_visible_text(your_name)
        if your_name != "---Your Name---":
            self.click_login_button()


