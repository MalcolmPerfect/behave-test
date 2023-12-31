import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given('navigate to "{url}"')
def navigate_to_url(context, url):
    logging.info(f"navigating to url {url}")

    browser = context.browser
    browser.get(url)
    # clear the "before you continue to google" popup if it shows itself
    browser.find_element(By.ID, "L2AGLb").click()


@when('search for the text "{search_text}"')
def step_impl(context, search_text):
    logging.debug(f"searching for {search_text}")

    browser = context.browser
    text_area = browser.find_element(By.NAME, "q")
    text_area.send_keys(search_text)
    text_area.send_keys(Keys.RETURN)


@then("search results are displayed")
def validate_results(context):
    logging.debug("validating results")

    browser = context.browser
    news_results = browser.find_element(By.XPATH, '//span[text()="Top stories"]')
    assert news_results.text == "Top stories"
