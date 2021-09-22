class Car(object):
  """
  Creates a car instance with a specified number.
  """

  def __init__(self, number):
    self.number = number

  def add_driver(self, driver):
    self.driver = driver
