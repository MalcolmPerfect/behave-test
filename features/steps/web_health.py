import logging
from bs4 import BeautifulSoup
import requests
from behave import given, when, then


@given('the sitemap "{sitemap_url}"')
def save_sitemap(context, sitemap_url: str):
    """save the sitemap url for use in the action step"""
    logging.debug(f"saving sitemap {sitemap_url}")
    context.sitemap = sitemap_url


@when("each location is requested")
def request_each_sitemap_location(context):
    """takes every location in the sitemap and checks it gets
    a 200. Using BS here might be overkill but useful lib for
    web scraping when no need for selenium"""
    r = requests.get(context.sitemap, timeout=5)

    sitemap_xml = r.text
    soup = BeautifulSoup(sitemap_xml, features="xml")
    site_tags = soup.find_all("loc")

    sitemap_register = {}

    for site in site_tags:
        try:
            logging.info(f"Requesting http status for site {site.string}")
            status_code = requests.get(site.string, timeout=5).status_code
            sitemap_register[site] = status_code
        except Exception as err:
            sitemap_register[site] = err
            logging.info(f"Error for {site}", exc_info=True)

    context.sitemap_register = sitemap_register


@then("all return status {status_code:Number}")
def validate_return_statuses(context, status_code: int):
    """Check the return statuses all match the supplied code."""
    sites_not_ok = {
        k: v for k, v in context.sitemap_register.items() if v != status_code
    }

    for site, code in sites_not_ok.items():
        logging.debug(f"{site}: {code}")

    assert len(sites_not_ok) == 0
