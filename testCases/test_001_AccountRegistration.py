import time

from selenium.webdriver.chrome import webdriver

from pageObjects.HomePage import Homepage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_AccountReg:
    baseUrl=ReadConfig.getApplicationUrl()
    logger=LogGen.loggen()

    def test_account_reg(self,setUp):
        self.logger.info("testcase started")
        self.driver=setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        time.sleep(6)

        self.hp=Homepage(self.driver)
        self.logger.info("clicking on MyAccount")
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.reg=AccountRegistrationPage(self.driver)
        self.reg.setFirstName("John")
        self.reg.setLastName("Candy")
        self.reg.setEmail("bhg7643@gmail.com")
        self.reg.setPassword("23421")
        self.reg.setPrivacyPolicy()
        self.reg.clickContinue()
        self.confmsg=self.reg.getConfirmationMsg()
        self.driver.close()
        if self.confmsg=="Your Account Has Been Created!":
            assert True
        else:
            self.logger.error("account registration is failed")
            assert False
        self.logger.info("testcase finished")
















































