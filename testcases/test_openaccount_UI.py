from pages.openaccountPage import OpenAccount

def test_openaccount_UI(driver):
    oc = OpenAccount(driver)
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    oc.click_bankmanager_login()
    oc.click_open_account()
    assert oc.openaccount_text() == "Open Account", "Expected title 'Open Account' not found"
    assert oc.customer_text() == "Customer :", "Expected text 'Customer :' not found"
    assert oc.customer_placeholder() == "---Customer Name---", "Customer placeholder mismatch"
    assert oc.currency_text() == "Currency :", "Expected text 'Currency :' not found"
    assert oc.currency_placeholder() == "---Currency---", "Currency placeholder mismatch"
    assert oc.process_button_text() == "Process", "Expected button text 'Process' not found"