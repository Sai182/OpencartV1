# import undetected_chromedriver as uc
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setUp():
    # driver=webdriver.Chrome(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    # options = uc.ChromeOptions()
    # options.add_argument("--no-sandbox")
    # driver = uc.Chrome(options=options)
    return driver









