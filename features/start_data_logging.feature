@Login
Feature: LoginFeature
    In order to test login function
    As a Project owner
    I want to login with correct username and password

  Background:
    Given I have navigated to Oceaview with url <aUrl>

   @X2
  Scenario Outline: Login OceaView siteweb
    Given I have entered <userName> into the user name
    And I have entered <password> into the password
    And I have connected a X2 with SN <module_sn>
    And I have checked connection of sensor <sensor_sn>

    When I press submit button
    And I have started data logging for sensor <sensor_sn_CRC> from module <module_sn>
    And I have sent init packet

    Then I have checked mission configuration period value is <period_value>

    Examples: Vertical
      | aUrl          |  https://multi.oceaview.com:8081  | https://multi.oceaview.com:8081  | https://multi.oceaview.com:8081  |
      | userName      | xingsir@gmail.com                 | xingtt@gmail.com                 |  xingXXX@gmail.com               |
      | password      | Oceasoft123@                      | Oceasoft123@                     | Oceasoft453@                     |
      | module_sn     | E40C030000AD                      |E40C030000FD                      |FF0C030000AD                      |
      | sensor_sn     | 00000637227A28                    |00000637227D28                    |G0000637227A28                    |
      | sensor_sn_CRC | 2D00000637227A28                  |2D0000063722DA28                  |7D00000637227A28                  |
      | period_value  | 60                                |70                                |30                                |

  @CatchErrorMessage
  Scenario Outline: login with wrong password
    Given I have entered <userName> into the user name
    And I have entered <password> into the password
    When I press submit button
    Then Login should fail

    Examples: Vertical
      | aUrl          | https://multi.oceaview.com:8081  |  https://multi.oceaview.com:8081 |
      | userName      | xingsir@gmail.com                |  aaa                             |
      | password      | wrongPassword                    |  bbb                             |