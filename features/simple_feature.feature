Feature: simple feature
    Scenario: simplest scenario
        Given this simple thing
        When this happens
        Then this is expected

    Scenario: convert parameter to an integer
        Parameters are by default parsed as strings. This is
        fine for most things tbh (can convert as you need to).
        This example uses parse to convert to an int

        Given there are 100 gherkins
        When I eat 88 gherkins
        Then there are 12 gherkins left
    
