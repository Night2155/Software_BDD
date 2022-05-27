import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants

Calculator_Path = 'http://127.0.0.1:2022/'  # 網頁路徑

scenarios("./calc_rule.feature")


@pytest.fixture
def browser():
    b = webdriver.Firefox()  # 開啟瀏覽器
    b.implicitly_wait(10)
    b.get(Calculator_Path)  # 輸入網址
    yield b
    b.quit()  # 關閉瀏覽器


@pytest.fixture
def cache():
    cache = [0, 0]
    yield cache


@when(parsers.parse('I enter "{phrase}" first'))
def Key_In(browser, phrase, cache):
    input_box = browser.find_element_by_name('input-box')
    input_box.send_keys(phrase)  # 第一次輸入測試資料
    calculate = browser.find_element_by_name('Calculate')
    calculate.click()
    result_label = browser.find_element_by_id('result-label')
    cache[0] = result_label.get_attribute('innerHTML')
    input_box.clear()


@when(parsers.parse('I enter "{phrase}" again'))
def Key_In(browser, phrase, cache):
    input_box = browser.find_element_by_name('input-box')
    input_box.send_keys(phrase)  # 再次輸入測試資料
    calculate = browser.find_element_by_name('Calculate')
    calculate.click()
    result_label = browser.find_element_by_id('result-label')
    cache[1] = result_label.get_attribute('innerHTML')
    input_box.clear()


@then('I get the same answer')
def results(cache):
    assert cache[0] == cache[1]  # 確認結果是否相同
