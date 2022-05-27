import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants

Calculator_Path = 'http://127.0.0.1:2022/'  # 網頁路徑

# Scenarios 預先想到的測試流程

scenarios('./basic_calc.feature')

# Fixtures
# Pytest_bdd 執行每一個scenarios 呼叫 fixture


@pytest.fixture
def browser():
    b = webdriver.Firefox()  # 開啟瀏覽器
    b.implicitly_wait(10)
    b.get(Calculator_Path)  # 輸入網址
    yield b
    b.quit()  # 關閉瀏覽器

# Given Steps


@given(parsers.parse('I enter "{phrase}"'))
def Key_In(browser, phrase):
    input_box = browser.find_element_by_name('input-box')
    input_box.send_keys(phrase)  # 輸入測試資料

# When Steps


@when(parsers.parse('I press "=" button'))
def Press_Button(browser):
    browser.find_element_by_name('Calculate').click()  # 按下 "=" 按鍵

# Then Steps


@then(parsers.parse('I get the answer "{phrase}"'))
def results(browser, phrase):
    result = browser.find_element_by_id('result-label')
    assert result.get_attribute('innerHTML') == phrase  # 確認結果是否相同
