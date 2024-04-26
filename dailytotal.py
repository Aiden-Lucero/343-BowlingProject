class DailyTotal:
  """
  Represents the total amount for the day.
  """

  def __init__(self):
      self.date = ""
      self.total_amount = 0.0

  def set_date(self, date: str) -> None:
      """
      Sets the date the lane is rented.
      """
      self.date = date

  def set_total(self, total: float) -> None:
      """
      Sets the total for the lane rented.
      """
      self.total_amount = total

  def get_total(self) -> float:
      """
      Retrieves the total amount for the day.
      """
      return self.total_amount

