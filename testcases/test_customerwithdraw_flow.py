import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.customerdepositPage import CustomerDepositPage
from pages.customerwithdrawlPage import CustomerWithdrawlPage
from pages.customerloginPage import CustomerloginPage
from read_data.datareader import Read

@pytest.mark.parametrize("amount,case", Read.get_csv_data('../testdata/withdrawamount.csv'))
def test_customer_withdraw(driver, amount, case):
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    cl = CustomerloginPage(driver)
    cl.customerloginpage("Harry Potter")

    # Deposit first if needed
    if case == "p":
        cd = CustomerDepositPage(driver)
        cd.customerdepositpage("200")
        driver.refresh()

    # Withdraw
    cw = CustomerWithdrawlPage(driver)
    cw.customerwithdrawlpage(amount)

    # Wait for message to appear
    try:
        message_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@ng-show='message']"))
        )
        message = message_element.text
    except Exception:
        message = ""

    print(f"Message after withdrawal: '{message}'")

    if case == 'p':
        assert "Transaction successful" in message, f"Expected success, got '{message}'"
    elif case == 'i':
        assert "Transaction Failed" in message, f"Expected insufficient funds, got '{message}'"
    elif case in ['e', 'n']:
        assert message == "", f"Expected no message, got '{message}'"
