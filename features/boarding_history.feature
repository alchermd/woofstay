Feature: Boarding History

  Scenario: A pet's boarding history is kept
    Given I empty the "Pets" table

    And I create the following pets:
      | name  | breed | type |
      | Cholo | Husky | Dog  |

    And I empty the "Hotels" table

    And I create the following hotels:
      | name       | hourly_rate |
      | MyPetHotel | 50          |

    And I empty the "BoardingRecords" table

    When I board "Cholo" to "MyPetHotel" at "07:30 AM"

    And "Cholo" checks out from "MyPetHotel" at "12:00 PM"

    And I board "Cholo" to "MyPetHotel" at "04:00 PM"

    And "Cholo" checks out from "MyPetHotel" at "08:00 PM"

    Then "2" records are saved on "Cholo"'s boarding history