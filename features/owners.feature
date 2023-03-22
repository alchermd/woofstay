Feature: Owner records

  Scenario: An Owner's record can be added into the system
    Given I empty the "Owners" table

    When I add "Micah" "Batayola", with contact "+123456789", and address "123 Easy Street" into the system

    And I add "Aljon" "Doloiras", with contact "+987654321", and address "123 Easy Street" into the system

    And I add "Beth", with contact "+88800088" into the system

    Then the following records are saved in the "Owners" table:
      | first_name | last_name | contact_number | address         |
      | Micah      | Batayola  | +123456789     | 123 Easy Street |
      | Aljon      | Doloiras  | +987654321     | 123 Easy Street |
      | Beth       | null      | +88800088      | null            |

  Scenario: A Pet's record can be associated with an Owner
    Given I empty the "Owners" table

    And I add "Micah" "Batayola", with contact "+123456789", and address "123 Easy Street" into the system

    And I empty the "Pets" table

    Then I add "Cholo" the "Husky" "Dog" into the system

    When I set "Micah" "Batayola" as "Cholo"'s owner

    Then I get "Micah" "Batayola"'s record when I fetch "Cholo"'s owner records