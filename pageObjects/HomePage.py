from selenium.webdriver.common.by import By

class Homepage:
    lnk_myAccount_xpath="//span[normalize-space()='My Account']"
    lnk_register_linktext="Register"
    lnk_login_linktext="Login"

    def __init__(self,driver):
        self.driver=driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.lnk_myAccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()





















