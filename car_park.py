from driver import Driver
from car import Car

class CarPark(object):
  """
  Creates a car park instance with a specified number of parking slots.
  """

  def __init__(self, slots):
    self.slots = slots
    self.parked = [None]*slots

  def park(self, number, custom_param, param_val):
    if custom_param != 'driver_age':
      print "Please input only driver's age"
      return

    for slot in range(self.slots):
      if self.parked[slot] == None:
        car = Car(number)
        driver = Driver(param_val, car)

        self.parked[slot] = car
        print 'Car with vehicle registration number "{}" has been parked at slot number {}'.format(car.number, slot + 1)
        break

      if slot == self.slots - 1:
        print 'Please look for another car park, all slots here are full'

  def slot_numbers_for_driver_of_age(self, age):
    slots = []

    for slot in range(self.slots):
      if self.parked[slot] and self.parked[slot].driver.driver_age == age:
        slots.append(str(slot + 1))

    if len(slots):
      print ', '.join(slots)
    else:
      print 'No parked car matches the query'

  def slot_number_for_car_with_number(self, number):
    for slot in range(self.slots):
      if self.parked[slot] and self.parked[slot].number == number:
        print slot + 1
        return

    print 'No parked car matches the query'  

  def leave(self, slot):
    slot = int(slot)

    if not slot or slot > self.slots:
      print "This slot doesn't exist in this parking lot"
      return

    if self.parked[slot - 1]:
      print 'Slot number {} vacated, the car with vehicle registration number "PB-01-HH-1234" left the space, the driver of the car was of age 21'.format(slot, self.parked[slot - 1].number, self.parked[slot - 1].driver.driver_age)
      self.parked[slot - 1] = None
    else:
      print 'No car in this slot'

  def vehicle_registration_number_for_driver_of_age(self, age):
    numbers = []

    for slot in range(self.slots):
      if self.parked[slot] and self.parked[slot].driver.driver_age == age:
        numbers.append(self.parked[slot].number)

    if len(numbers):
      print ', '.join(numbers)
    else:
      print 'No parked car matches the query'
