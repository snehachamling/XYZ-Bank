import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.customerloginPage import CustomerloginPage
from read_data.datareader import Read

@pytest.mark.parametrize("your_name,case", Read.get_csv_data('../testdata/customerlogin.csv'))
def test_customerlogin(driver,your_name,case):
    cl = CustomerloginPage(driver)
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    cl.customerloginpage(your_name)

    if case == 'p':
        expected = "Harry Potter"
        welcome_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='fontBig ng-binding']"))
        )
        actual = welcome_text.text
        assert expected == actual, f"Expected welcome '{expected}', got '{actual}'"

    else:
        try:
            login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
            assert not login_button.is_displayed(), "Expected Login button to disappear, but it is still visible."
        except NoSuchElementException:
            # This is also OK - means button is gone
            pass

