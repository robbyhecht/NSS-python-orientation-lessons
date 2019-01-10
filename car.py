from vehicle import Vehicle

class Car(Vehicle):

# by defining our specific init method on a car class, the python interpreter will call it when we make an instance of a Car, but it only will call one init method. So the vehicle init method will not be automatically called. We have to manually call it in the car init method so that we create a proper instance of a Vehicle.

  def __init__(self, price, ab_count, material="cloth"):
    self.price = price
    self.airbag_count = ab_count
    self.seat_material = material
    super().__init__("car")

  def calc_payments(self, months, rate):
    return f'Your payments for a purchase price of ${self.price} over {months} at {rate} would be too high. Buy something cheaper.'

