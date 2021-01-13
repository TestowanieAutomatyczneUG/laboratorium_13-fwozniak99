Feature: FizzBuzz Functionality
  Scenario: Number divisible by 15
    Given we have an instance of FizzBuzz
    When the number is 15
    Then returned value will be FizzBuzz

  Scenario: Number divisible by 5
    Given we have an instance of FizzBuzz
    When the number is 5
    Then returned value will be Buzz

  Scenario: Number divisible by 3
    Given we have an instance of FizzBuzz
    When the number is 3
    Then returned value will be Fizz

  Scenario: Number not divisible by neither 3 nor 5
    Given we have an instance of FizzBuzz
    When the number is 4
    Then returned value will be 4

  Scenario Outline: Numbers divisible by 15
    Given we have an instance of FizzBuzz
    When the number is <number>
    Then returned value will be <result>
    Examples:
      | number | result |
      |     15 | FizzBuzz |
      |     30 | FizzBuzz |
      |     45 | FizzBuzz |
