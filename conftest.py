from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
