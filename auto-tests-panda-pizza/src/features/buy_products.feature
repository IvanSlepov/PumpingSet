Feature: Check if pizza can be ordered on the PandaPizza page

#  Scenario: Ordering pizza
#    Given User proceeds to the Panda Pizza main page
#    Then If there's a blocking message, they close it
#    Then They proceed to the Pizza Page
#    Then They choose some pizza and add it to the cart

  Scenario: Checking out pizza
    Given User proceeds to the Panda Pizza main page
    Then If there's a blocking message, they close it
    Then They proceed to the Pizza Page
    Then They choose some pizza and add it to the cart
    Then User opens the order cart
    Then User continues with checkout if required product is in cart
    Then User populates the required data and places the order
    Then User waits for the placed order confirmation

#  Scenario: Checking out sushi set
#    Given User proceeds to the Panda Pizza main page.
#    Then If there's a blocking message, they close it.
#    Then They proceed to the Sushi Page.
#    Then If there's another blocking message, they close it.
#    Then They choose some sushi set and add it to the cart.
#    Then User opens the order cart.
#    Then User continues with checkout if required product is in cart.
##    Then User populates the required data and places the order.
##    Then User waits for the placed order confirmation.