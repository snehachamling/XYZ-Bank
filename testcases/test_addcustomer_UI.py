from pages.addcustomerPage import Addcustomer

def  test_addcustomer_UI(driver):
    ac = Addcustomer(driver)
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    ac.click_bankmanager_login()
    ac.click_add_customer()
    assert ac.add_customer_text() == "Add Customer", "Expected title 'Add Customer' not found"
    assert ac.first_name_text() == "First Name :"
    assert ac.first_name_placeholder() == "First Name", "First Name placeholder mismatch"
    assert ac.last_name_text() == "Last Name :"
    assert ac.last_name_placeholder() == "Last Name", "Last Name placeholder mismatch"
    assert ac.post_code_text() == "Post Code :"
    assert ac.post_code_placeholder() == "Post Code", "Post Code placeholder mismatch"
    assert ac.submit_button_text() == "Add Customer"

