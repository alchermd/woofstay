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

  Scenario: A pet's boarding fee is computed by how many hours they stayed
    Given I empty the "Pets" table

    And I create the following pets:
      | name  | breed |
      | Cholo | Husky |

    And I empty the "Hotels" table

    And I create the following hotels:
      | name       | hourly_rate |
      | MyPetHotel | 50          |

    When I board "Cholo" to "MyPetHotel" at "07:30 AM"

    And "Cholo" checks out from "MyPetHotel" at "12:00 AM"

    Then "Cholo"'s boarding fee for his stay at "MyPetHotel" would be "225"