from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def is_element_present(browser, how, what, timeout=4):
    try:
        WebDriverWait(browser, timeout).until(EC.presence_of_element_located((how, what)))
    except TimeoutException:
        return False

    return True


def test_should_be_button_add_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button_add_to_basket = is_element_present(browser, By.CSS_SELECTOR, 'button.btn-add-to-basket')

    language = browser.execute_script("return window.navigator.userLanguage || window.navigator.language")
    
    assert button_add_to_basket, f'The button will suck, with the option language {language}'



