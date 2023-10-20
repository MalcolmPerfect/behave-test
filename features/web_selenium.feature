@browser.chrome
Feature: web with selenium
    Simple example of web automation using selenium with behave,
    just for learning purposes. The chrome browser is setup and
    torn down at the feature level

  Scenario: simple search
        Simple search on google

    Given navigate to "https://www.google.co.uk"
    When search for the text "news"
    Then search results are displayed

