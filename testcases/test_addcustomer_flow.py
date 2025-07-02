import pytest

from pages.addcustomerPage import Addcustomer
from read_data.datareader import Read

@pytest.mark.parametrize("first_name,last_name,post_code,case", Read.get_csv_data('../testdata/addcustomer.csv'))
def test_addcustomer(driver,first_name,last_name,post_code,case):
    ac = Addcustomer(driver)
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    ac.addcustomerpage(first_name,last_name,post_code)

    if case == 'p':
        expected = "Customer added successfully with customer id :"
        actual = driver.switch_to.alert.text
        driver.switch_to.alert.accept()
        assert actual.startswith(expected), f"Expected alert starting with '{expected}', got '{actual}'"

    elif case == 'e':
        assert driver.execute_script("return arguments[0].validity.valueMissing;", ac.first_name()) is True
        assert driver.execute_script("return arguments[0].validity.valueMissing;", ac.last_name()) is True
        assert driver.execute_script("return arguments[0].validity.valueMissing;", ac.post_code()) is True

    else:
        expected = "Please check the details. Customer may be duplicate."
        actual = driver.switch_to.alert.text
        driver.switch_to.alert.accept()
        assert expected == actual, f"Expected alert '{expected}', got '{actual}"



