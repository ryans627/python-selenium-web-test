import pytest
from selenium import webdriver
import time


# 前后置夹具
@pytest.fixture()
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()


def test_login(driver):
    time.sleep(3)
