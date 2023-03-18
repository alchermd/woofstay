Feature: Pet records

  Scenario: A pet's record can be added into the system
    Given I empty the "Pets" table

    When I add "Cholo" the "Husky" "Dog" into the system

    And I add "Jodie" the "Bully" "Dog" into the system

    Then the following records are saved in the "Pets" table:
      | name  | breed | type |
      | Cholo | Husky | Dog  |
      | Jodie | Bully | Dog  |