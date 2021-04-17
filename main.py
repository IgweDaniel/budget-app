class Category:
  def __init__(self, category): 
        self.ledger =[]
        self.amount=0
        self.category = category 


  def check_funds(self,amount):
    if self.amount< amount:
      return False
    else:
      return True


  def deposit(self,amount, description=""):
    self.ledger.append({"amount":amount,"description":description})
    self.amount += amount


  def withdraw(self,amount,description=""):
    if self.check_funds(amount) ==True:
      self.amount -=amount
      self.ledger.append({"amount":-amount,"description":description})
      return True
    else:
      return False

  # return balanace of budget 
  def get_balance(self):
    return self.amount
    
  def transfer(self,amount,category):

    if self.check_funds(amount)==True:

      self.amount-=amount

      self.ledger.append({"amount": -amount,"description":"Transfer to "+category.category})

      category.ledger.append({"amount": amount,"description": "Transfer from "+self.category})

      return True

    else:

      return False
