import logging
from selenium import webdriver
from behave import fixture, use_fixture


def init_logging(context):
    context.config.setup_logging(configfile="logging.conf")
    logging.info(f"Logging configured for {logging.getLevelName(logging.root.level)}")


def before_all(context):
    init_logging(context)


def before_feature(context, feature):
    logging.info(f"Running feature {feature.name}")
    logging.info(f"Feature tags {feature.tags}")

    if "browser.chrome" in feature.tags:
        logging.info("tag found!!")
        use_fixture(init_chrome, context)


def before_scenario(context, scenario):
    logging.info(f"before scenario {scenario.name}")


def after_scenario(context, scenario):
    logging.info(f"after scenario {scenario.name}")


@fixture
def init_chrome(context):
    """initialise chrome and set the cleanup, which
    is executed when the context is removed"""
    logging.info("initialising chrome")
    browser = webdriver.Chrome()
    # driver.implicitly_wait(2)
    context.browser = browser
    context.add_cleanup(quit_browser(browser))
    return browser


def quit_browser(browser):
    """wrap around quit driver so we can see in the logs that it's
    quitting at the expected time"""

    def _wrapper():
        logging.info("quitting browser")
        browser.quit()

    return _wrapper
