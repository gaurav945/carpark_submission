import sys
from car_park import CarPark
from driver import Driver
from car import Car

instruction_file = open(sys.argv[1], 'r')

instructions = instruction_file.read().splitlines()

# creating car park
# FAQs ensured that Create_parking_lot will always be at the top of the file
parking_slots = int(instructions[0].split()[-1])

if parking_slots:
  new_car_park = CarPark(int(instructions[0].split()[-1]))

  print 'Created parking of {} slots.'.format(new_car_park.slots)

  for counter in range(1, len(instructions)):
    if instructions[counter]:
      function_call = instructions[counter].split()[0]
      function_arg = instructions[counter].split()[1:]

      getattr(new_car_park, function_call.lower()) (*function_arg)
else:
  print 'This car park is not functional yet'

















"""
- they might add new functions to car park
- they might new attributes to a car
- arguments to an existing function might change
- is it possible they could change the instruction order in the future ?
- instead of adding a query type all the time
- 
"""