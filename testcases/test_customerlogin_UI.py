from pages.customerloginPage import CustomerloginPage

def test_customerlogin_UI(driver):
    cl = CustomerloginPage(driver)
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    cl.click_customer_login()
    cl.customerloginpage("Harry Potter")
    cl.click_login_button()
    assert cl.welcome_text() == "Welcome Harry Potter !!", "Expected welcome text not found"
    assert cl.account_number() == "1004", "Expected account number not found"
    balance_text = cl.balance()
    assert balance_text != "", "Balance should not be empty"
    assert balance_text.isdigit(), f"Balance should be a number, got '{balance_text}'"
    assert cl.currency() == "Dollar", "Expected currency 'Dollar' not found"
    assert cl.transactions_text() == "Transactions", "Expected text 'Transactions' not found"
    assert cl.deposit_text() == "Deposit", "Expected text 'Deposit' not found"
    assert cl.withdrawl_text() == "Withdrawl", "Expected text 'Withdrawl' not found"