import pytest
from selenium.common.exceptions import NoAlertPresentException
from pages.openaccountPage import OpenAccount
from read_data.datareader import Read

@pytest.mark.parametrize("customer_name,currency,case", Read.get_csv_data('../testdata/openaccount.csv'))
def test_open_account(driver, customer_name, currency, case):
    oa = OpenAccount(driver)
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    oa.openaccountpage(customer_name, currency)

    try:
        alert = driver.switch_to.alert
        actual = alert.text
        alert.accept()
    except NoAlertPresentException:
        actual = None

    if case == 'p':
        expected = "Account created successfully with account Number :"
        assert actual is not None, "Expected success alert but no alert was present"
        assert actual.startswith(expected), f"Expected alert starting with '{expected}', got '{actual}'"
    else:
        # we actually expect NO alert
        assert actual is None, f"Expected NO alert, but got alert with text '{actual}'"
