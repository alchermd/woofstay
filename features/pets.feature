Feature: Pet records

  Scenario: A pet's record can be added into the system
    Given I empty the "Pets" table

    When I add "Cholo" the "Husky" into the system

    And I add "Jodie" the "Bully" into the system

    Then the following records are saved in the "Pets" table:
      | name  | breed |
      | Cholo | Husky |
      | Jodie | Bully |