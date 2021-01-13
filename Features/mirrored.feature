Feature: Testing Mirrored class / it checks if a first given word is a mirror reflection
  of the second given word

  @mirror
  Scenario: Two mirrored words
    Given two words
    """
    kot,tok
    """
    When they are mirrored and same length
    Then returned value should be True

  @mirror
  Scenario: Two not mirrored words
    Given two words
    """
    kod,tok
    """
    When they are not mirrored and same length
    Then returned value should be False

  @mirror
  Scenario: Two words where first one is longer
    Given two words
    """
    szczur,idol
    """
    When they are not mirrored and first is longer
    Then returned value should be "Words aren't the same length"

  @mirror
  Scenario: Two words where second one is longer
    Given two words
    """
    pies,piesek
    """
    When they are not mirrored and second is longer
    Then returned value should be "Words aren't the same length"

  @mirror
  Scenario: Two words where first one is an int
    Given two words
    """
    123,piesek
    """
    When they are not mirrored and first is an int
    Then returned value should be "Cannot be an integer"

  @mirror
  Scenario: Two words where second one is an int
    Given two words
    """
    word,456
    """
    When they are not mirrored and second is an int
    Then returned value should be "Cannot be an integer"

  @mirror
  Scenario: Two words where first one is boolean
    Given two words
    """
    True,word
    """
    When they are not mirrored and first is boolean
    Then returned value should be "Must be a string"

  @mirror
  Scenario: Two words where second one is boolean
    Given two words
    """
    word,False
    """
    When they are not mirrored and second is boolean
    Then returned value should be "Must be a string"