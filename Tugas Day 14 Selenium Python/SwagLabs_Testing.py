import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_failed_login_with_empty_email(self): 
        # steps
        browser = self.browser 
        browser.get("https://www.saucedemo.com/")
        time.sleep(1)
        browser.find_element(By.ID,"user-name").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.CSS_SELECTOR,".error-message-container").text

        self.assertEqual(response_message, 'Epic sadface: Username is required')
    
    def test_failed_login_with_empty_password(self): 
        # steps
        browser = self.browser 
        browser.get("https://www.saucedemo.com/")
        time.sleep(1)
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.CSS_SELECTOR,".error-message-container").text

        self.assertEqual(response_message, 'Epic sadface: Password is required')
    
    def test_failed_login_with_empty_email_and_password(self): 
        # steps
        browser = self.browser 
        browser.get("https://www.saucedemo.com/")
        time.sleep(1)
        browser.find_element(By.ID,"user-name").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.CSS_SELECTOR,".error-message-container").text

        self.assertEqual(response_message, 'Epic sadface: Username is required')
    
    def test_success_login(self): 
        # steps
        browser = self.browser 
        browser.get("https://www.saucedemo.com/") 
        time.sleep(1)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") 
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

    def test_success_checkout(self): 
        # steps
        browser = self.browser 
        browser.get("https://www.saucedemo.com/") 
        time.sleep(1)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") 
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,".shopping_cart_link").click()
        time.sleep(1)
        browser.find_element(By.ID,"checkout").click()
        time.sleep(1)
        browser.find_element(By.ID,"first-name").send_keys("Kamisato") 
        time.sleep(1)
        browser.find_element(By.ID,"last-name").send_keys("Kakeru") 
        time.sleep(1)
        browser.find_element(By.ID,"postal-code").send_keys("73516") 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"html body div#root div#page_wrapper.page_wrapper div#contents_wrapper div#checkout_info_container.checkout_info_container div.checkout_info_wrapper form div.checkout_buttons input#continue.submit-button.btn.btn_primary.cart_button.btn_action").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#finish").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"html body div#root div#page_wrapper.page_wrapper div#contents_wrapper div#checkout_complete_container.checkout_complete_container button#back-to-products.btn.btn_primary.btn_small").click()
        time.sleep(1)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()