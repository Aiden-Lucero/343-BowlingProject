class Transaction:
  """
  Represents a transaction for renting a lane.
  """

  def __init__(self):
    self.date = ""
    self.customer_start_rental = ""
    self.customer_name = ""
    self.lane_number = ""
    self.customer_end_rental = ""

  def set_name(self, name: str) -> None:
    """
      Sets the name of the customer.
      """
    self.customer_name = name

  def set_lane_start_time(self, time: int) -> None:
    """
      Sets the start time for the customer's lane.
      """
    self.customer_start_rental = time

  def get_lane(self, lane_number: int) -> int:
    """
      Retrieves the lane number assigned to the customer.
      """
    return self.lane_number

  def get_date(self) -> str:
    """
      Retrieves the date of the transaction.
      """
    return self.date

  def set_lane_end_time(self, time: int) -> None:
    """
      Sets the end time for the customer's lane.
      """
    self.customer_end_rental = time
