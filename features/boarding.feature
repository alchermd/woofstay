Feature: Pet boarding
  Scenario: A pet can be boarded to a hotel
    Given I empty the "Pets" table

    And I create the following pets:
      | name  | breed |
      | Cholo | Husky |

    And I empty the "Hotels" table

    And I create the following hotels:
      | name       |
      | MyPetHotel |

    When I board "Cholo" to "MyPetHotel"

    Then "Cholo" is boarded