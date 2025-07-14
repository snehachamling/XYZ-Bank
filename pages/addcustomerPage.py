
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Addcustomer:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_locator = (By.XPATH, "//input[@ng-model='fName']")
        self.last_name_locator = (By.XPATH, "//input[@ng-model='lName']")
        self.post_code_locator = (By.XPATH, "//input[@ng-model='postCd']")

    def bankmanager_login_text(self):
        wait = WebDriverWait(self.driver, 10)
        title = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/button")))
        return title.text

    def bankmanager_login(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/button")))

    def click_bankmanager_login(self):
        self.bankmanager_login().click()

    def add_customer_text(self):
        wait = WebDriverWait(self.driver, 10)
        title = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/button[1]")))
        return title.text

    def add_customer(self):
        wait = WebDriverWait(self.driver,10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/button[1]")))

    def click_add_customer(self):
        self.add_customer().click()

    def first_name_text(self):
        wait = WebDriverWait(self.driver,10)
        title = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/label')))
        return title.text

    def first_name_placeholder(self):
        return self.driver.find_element(*self.first_name_locator).get_attribute("placeholder")

    def first_name(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input")))

    def enter_first_name(self, first_name):
        self.first_name().send_keys(first_name)

    def last_name_text(self):
        title = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/label')
        return title.text

    def last_name_placeholder(self):
        return self.driver.find_element(*self.last_name_locator).get_attribute("placeholder")

    def last_name(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input")

    def enter_last_name(self, last_name):
        self.last_name().send_keys(last_name)

    def post_code_text(self):
        title = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/label')
        return title.text

    def post_code_placeholder(self):
        return self.driver.find_element(*self.post_code_locator).get_attribute("placeholder")

    def post_code(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input")

    def enter_post_code(self, post_code):
        self.post_code().send_keys(post_code)

    def submit_button_text(self):
        title = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button')
        return title.text

    def submit_button(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/button")

    def click_submit(self):
        self.submit_button().click()

    def addcustomerpage(self, first_name, last_name, post_code):
        self.click_bankmanager_login()
        self.click_add_customer()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_post_code(post_code)
        self.click_submit()




