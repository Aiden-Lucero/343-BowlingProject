class DailyTotal:
  """
  Represents the total amount for the day.
  """

  def __init__(self):
      self.date = ""
      self.total_amount = 0.0
      self.transactions = []

  def set_date(self, date: str) -> None:
      """
      Sets the date the lane is rented.
      """
      self.date = date

  def get_total(self) -> float:
      """
      Retrieves the total amount for the day.
      """
      return self.total_amount

  def get_transactions(self) -> list:
      """
      Retrieves the list of transactions for the day.
      """
      return self.transactions