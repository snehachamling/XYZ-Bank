import pytest
from pages.customersPage import CustomersPage

def test_customers(driver):
    cp = CustomersPage(driver)
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    cp.customerpage("Harry")


