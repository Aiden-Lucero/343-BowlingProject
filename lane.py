class Lane:
  """
  Represents a lane for renting.
  """

  def __init__(self):
      self.lane_number = 0
      self.hourly_lane_cost = 0.00
      
      #transaction already has start and end time
      #self.customer_start_rental = ""
      #self.customer_end_rental = ""
  def set_lane_number(self, number: int) -> None:
    """
    Assigns the lane number to the customer.
    """
    self.lane_number = number


    
  def set_hourly_lane_cost(self, amount: float) -> None:
      """
      Sets the hourly rate for the lane.
      """
      self.hourly_lane_cost = amount

  
  def get_hourly_lane_cost(self) -> float:
      """
      Retrieves the hourly rate for the lane.
      """
      return self.hourly_lane_cost

  def get_lane_number(self) -> int:
      """
      Retrieves the lane number assigned to the customer.
      """
      return self.lane_number

  

  def get_total(self, hourly: float, startT: int, endT: int) -> float:
      """
      Retrieves the total amount for the day.
      """
      return hourly * (endT - startT)
      