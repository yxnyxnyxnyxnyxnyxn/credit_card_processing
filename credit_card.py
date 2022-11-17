class CreditCard:
  def __init__(self,card_number, limit):
    if self.isValid(card_number):
      self.card_number = card_number
      self.balance = 0
      self.limit = limit
      self.isValid = True
    else:
      self.isValid = False 
      self.balance = "error"  

  def isValid(self,card_number):
    n_digits = len(card_number)
    n_sum = 0
    is_second = False
     
    for i in range(n_digits - 1, -1, -1):
        d = ord(card_number[i]) - ord('0')
     
        if (is_second == True):
            d = d * 2
  
        # We add two digits to handle
        # cases that make two digits after
        # doubling
        n_sum += d // 10
        n_sum += d % 10
  
        is_second = not is_second
     
    if (n_sum % 10 == 0):
        return True
    else:
        return False
