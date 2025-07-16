import pytest
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.customerloginPage import CustomerloginPage
from pages.customerdepositPage import CustomerDepositPage
from read_data.datareader import Read

@pytest.mark.parametrize("amount,case", Read.get_csv_data('../testdata/depositamount.csv'))
def test_customer_deposit(driver, amount, case):
    cl = CustomerloginPage(driver)
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    cl.customerloginpage("Harry Potter")
    cd = CustomerDepositPage(driver)
    cd.customerdepositpage(amount)

    try:
        message_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[@ng-show='message']"))
        )
        message = message_element.text.strip()
        if not message:
            message = ""
    except (TimeoutException, NoSuchElementException):
        message = ""

    if case == 'p':
        assert "Deposit Successful" in message, f"Expected success message, got '{message}'"
    else:
        assert message == "", f"Expected no message, got '{message}'"
