class Transaction: 
  """
  Represents a transaction for renting a lane.
  """

  def __init__(self):
    self.date = ""
    self.customer_start_rental = 0
    self.customer_name = ""
    self.lane_number = 0
    self.customer_end_rental = 0

  def set_name(self, name: str) -> None:
    """
      Sets the name of the customer.
      """
    self.customer_name = name

  def get_name(self) -> str:
    """
    Retrieves the name of the customer.
    """
    return self.customer_name

  def set_start_time(self, time: int) -> None:
    """
      Sets the start time for the customer's lane.
      """
    self.customer_start_rental = time

  def set_lane_number(self, number: int) -> None:
    """
    Assigns the lane number to the customer.
    """
    self.lane_number = number
  
  def get_lane_number(self) -> int:
    """
      Retrieves the lane number assigned to the customer.
      """
    return self.lane_number

  def get_start_time(self) -> int:
    """
    Retrieves the start time for the customer's lane.
    """
    return self.customer_start_rental

  def set_date(self, date: str) -> None:
    """
    Sets the date of the transaction.
    """ 
    self.date = date
  
  def get_date(self) -> str:
    """
      Retrieves the date of the transaction.
      """
    return self.date

  def set_end_time(self, time: int) -> None:
    """
      Sets the end time for the customer's lane.
      """
    self.customer_end_rental = time

  def get_end_time(self) -> int:
    """
    Retrieves the end time for the customer's lane.
    """
    return self.customer_end_rental