@Login
Feature: LoginFeature
    In order to test login function with wrong username or password
    As a Project owner


  @CatchErrorMessage
  Scenario Outline: login with wrong password part 2
    Given I have navigated to Oceaview with url <aUrl>
    And I have entered <userName> into the user name
    And I have entered <password> into the password
    When I press submit button
    Then Login should fail

    Examples: Vertical
      | aUrl          | https://multi.oceaview.com:8081  |  https://multi.oceaview.com:8081 | https://multi.oceaview.com:8081 |
      | userName      |            <default>             |  xxx                             | yyy                             |
      | password      |            <default>             |  ddd                             | ttt                             |