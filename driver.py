class Driver(object):
  """
  Creates a driver instance with a specified age & associates a car instance with it.
  """

  def __init__(self, age, car):
    self.driver_age = age
    self.car = car

    self.car.add_driver(self)
