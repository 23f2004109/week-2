import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_email_is_decoded(driver):
    # Get the absolute path to the HTML file
    file_path = os.path.abspath('index.html')
    # Load the HTML file
    driver.get(f'file://{file_path}')
    # Find the email link
    email_link = driver.find_element(By.TAG_NAME, 'a')
    # Check that the email is correctly decoded
    assert email_link.text == '23f2004109@ds.study.iitm.ac.in'
