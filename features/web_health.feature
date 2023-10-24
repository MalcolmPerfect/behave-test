Feature: web health

    Scenario: all destinations listed in the sitemap are available
        Given the sitemap "https://www.nsandi.com/sitemap.xml"
        When each location is requested
        Then all return status 200

