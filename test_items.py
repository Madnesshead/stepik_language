from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert button, '"Add to basket" button was not found'
