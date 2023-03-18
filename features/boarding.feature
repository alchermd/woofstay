Feature: Pet boarding

  Scenario: A pet can be boarded to a hotel
    Given I empty the "Pets" table

    And I create the following pets:
      | name  | breed | type |
      | Cholo | Husky | Dog  |

    And I empty the "Hotels" table

    And I create the following hotels:
      | name       |
      | MyPetHotel |

    When I board "Cholo" to "MyPetHotel"

    Then "Cholo" is boarded

  Scenario: A pet's boarding fee is computed by how many hours they stayed
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

    Then "Cholo"'s boarding fee for his stay at "MyPetHotel" would be "225"

  Scenario: A pet is boarded on an invalid time
    Given I empty the "Pets" table

    And I create the following pets:
      | name  | breed | type |
      | Cholo | Husky | Dog  |

    And I empty the "Hotels" table

    And I create the following hotels:
      | name       | hourly_rate |
      | MyPetHotel | 50          |

    And I empty the "BoardingRecords" table

    When I board "Cholo" to "MyPetHotel" at "12:66 PM"

    Then I get an error saying that the given time is invalid

  Scenario: A pet is checked out on an invalid time
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

    And "Cholo" checks out from "MyPetHotel" at "12:66 AM"

    Then I get an error saying that the given time is invalid

  Scenario: A pet's boarding fee is independently computed from other pets
    Given I empty the "Pets" table

    And I create the following pets:
      | name  | breed | type |
      | Cholo | Husky | Dog  |
      | Jodi  | Bully | Dog  |

    And I empty the "Hotels" table

    And I create the following hotels:
      | name       | hourly_rate |
      | MyPetHotel | 50          |

    And I empty the "BoardingRecords" table

    When I board "Cholo" to "MyPetHotel" at "07:30 AM"
    And I board "Jodi" to "MyPetHotel" at "10:30 AM"

    And "Cholo" checks out from "MyPetHotel" at "12:00 PM"
    And "Jodi" checks out from "MyPetHotel" at "01:00 PM"

    Then "Cholo"'s boarding fee for his stay at "MyPetHotel" would be "225"